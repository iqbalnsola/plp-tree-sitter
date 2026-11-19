# Tugas 1 — Membaca Pohon (Tree-sitter + Python)

Praktikum PLP — Tugas 1 dari materi Tree-sitter. Folder ini **hanya** memuat Tugas 1
(membaca pohon, node bernama vs anonim, ERROR/MISSING).

## Isi

| File | Isi |
| --- | --- |
| `t1.py` | Skrip utama: parse 3 potongan kode, cetak pohon, cetak node anonim, uji ERROR |
| `t1b_missing.py` | Pembanding: kode JavaScript rusak yang menghasilkan `MISSING ")"` |
| `pohon-perkiraan.txt` | Pohon yang saya perkirakan **sebelum** run + selisihnya dengan hasil nyata |
| `out/t1.txt` | Keluaran nyata `t1.py` |
| `out/t1b_missing.txt` | Keluaran nyata `t1b_missing.py` |

## Pasang (sekali saja)

```bash
uv venv .venv
uv pip install --python .venv/Scripts/python.exe tree-sitter tree-sitter-python tree-sitter-javascript
```

Alternatif dengan pip biasa:

```bash
python -m venv .venv
.venv/Scripts/pip install tree-sitter tree-sitter-python tree-sitter-javascript
```

## Jalankan

```bash
.venv/Scripts/python.exe t1.py
```

Di Windows bisa juga klik dua kali `run.bat`.

## Yang ditunjukkan

1. **Tiga potongan kode** (fungsi, if/else, kelas) → pohonnya masing-masing.
2. **Node bernama vs anonim**: `def`, `:`, `(`, `)`, `,` tidak tampil di S-expression
   default, tapi tetap ada dan bisa dicetak lewat `children` + `is_named`.
3. **Kode dirusak** → node `ERROR`. Di grammar Python, menghapus `:` maupun `)`
   sama-sama menghasilkan `ERROR`, bukan `MISSING`. `MISSING` muncul di grammar
   JavaScript (`t1b_missing.py`), jadi keberadaan `ERROR`/`MISSING` bergantung grammar.

## Selesai jika

Bisa menjelaskan beda `children` dan `named_children` dengan contoh dari kode sendiri:

- `children` = semua anak, termasuk token anonim (`def`, `:`, `(`, `)`, `,`)
- `named_children` = hanya node yang punya nama di grammar (`identifier`,
  `parameters`, `block`) — inilah yang tampil di S-expression

## Kerja bareng (Tugas 2 dst.)

- **Tugas 1** dikerjakan Muhammad Iqbal (`iqbalnsola`), ada di root folder ini.
- **Tugas 2 (penjelajah node)** taruh di folder `tugas2/` agar tidak bentrok:
  `tugas2/jelajah.py`, `tugas2/kecil.py`, dan hasilnya `tugas2/out/`.
- Sebelum mulai: `git pull` dulu. Selesai satu langkah: commit dengan pesan
  spesifik, misalnya `Tugas 2: penjelajah rekursif dengan field dan posisi`,
  lalu `git push`. Jangan satu commit besar di akhir.
- Jalankan skrip pakai venv masing-masing (`.venv/` tidak ikut ter-commit),
  jadi pasang dulu: `uv venv .venv && uv pip install --python
  .venv/Scripts/python.exe tree-sitter tree-sitter-python tree-sitter-javascript`

