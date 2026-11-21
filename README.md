# Tugas 1: Membaca Pohon Tree-sitter

Tugas 1 praktikum PLP. Parse potongan kode Python pakai tree-sitter, lalu baca pohon yang dihasilkan.

## Cara jalan

```bash
git clone https://github.com/iqbalnsola/plp-tree-sitter.git
cd plp-tree-sitter
uv venv .venv
uv pip install --python .venv/Scripts/python.exe tree-sitter tree-sitter-python tree-sitter-javascript
.venv/Scripts/python.exe tugas1-3/t1/t1.py
```

Di Windows bisa juga dobel klik `run.bat`.

Kalau tidak pakai `uv`, ganti dua baris tengahnya dengan:

```bash
python -m venv .venv
.venv/Scripts/pip install tree-sitter tree-sitter-python tree-sitter-javascript
```

## Isi folder

Semua skrip dan bukti output ada di `tugas1-3/`, satu subfolder per tugas.

`tugas1-3/t1/t1.py` — Tugas 1 (Iqbal)
Parse tiga potongan kode (fungsi, if/else, kelas) dan cetak pohonnya. Lalu cetak anak-anak node `function_definition` dan `parameters` untuk membedakan node bernama dan anonim. Terakhir parse dua kode yang sengaja dirusak.

`tugas1-3/t1/t1b_missing.py` — Tugas 1 (Iqbal)
Kode JavaScript yang kurung tutupnya hilang. Ini yang memunculkan node `MISSING`.

`tugas1-3/t1/pohon-perkiraan.txt` — Tugas 1 (Iqbal)
Pohon yang saya tulis sebelum skrip dijalankan, termasuk dua tebakan yang ternyata salah.

`tugas1-3/t1/out/` — Tugas 1
Hasil run sebagai bukti: `t1.txt` dan `t1b_missing.txt`.

`tugas1-3/t2/jelajah.py` — Tugas 2 (Akmal)
Penjelajah node versi rekursif dan versi `TreeCursor`. Jalankan `python tugas1-3/t2/jelajah.py tugas1-3/t2/kecil.py`; tambahkan `--cursor` untuk versi TreeCursor.

`tugas1-3/t2/kecil.py` dan `tugas1-3/t2/contoh_nyata.py` — Tugas 2
Berkas uji: satu baris, dan file Python nyata 166 baris.

`tugas1-3/t2/out/` — Tugas 2
Hasil run sebagai bukti: `hasil_rekursif.txt` dan `hasil_cursor.txt`.

Tugas 3 nanti masuk ke `tugas1-3/t3/`: `q.py`, `q_params.py`, berkas `.scm`, dan `out/`.

## Yang perlu diperhatikan di output

Node anonim tidak ikut tercetak di S-expression. `def`, titik dua, `(`, `)`, dan `,` tetap ada di pohon, tapi hanya kelihatan kalau dicetak lewat `children` dan `is_named`. Ini juga beda antara `children` (semua anak) dan `named_children` (hanya yang bernama, dan itulah yang tampil di S-expression).

Dua tebakan awal saya salah. `panjang * lebar` ternyata `binary_operator` dengan field `left` dan `right`, bukan satu node biasa. `self.nama` ternyata `attribute` yang berisi `object` dan `attribute`, bukan `identifier`.

Soal node rusak: menghapus `:` atau `)` di Python sama-sama menghasilkan `ERROR`, bukan `MISSING`. `MISSING` baru muncul di grammar JavaScript, terlihat di `t1b_missing.py` sebagai `MISSING ")"` pada 1:18. Jadi keberadaan keduanya bergantung pada grammar yang dipakai.

## Pembagian kerja

- Tugas 1: Muhammad Iqbal (`iqbalnsola`)
- Tugas 2: Muhamad Akmal Rizqillah
- Tugas 3: Muhammad Iqbal
- Tugas 4 dan 5: Muhamad Akmal Rizqillah
- Tugas 6: Muhammad Iqbal

Struktur folder mengikuti modul, bukan per orang: `tugas1-3/` (subfolder `t1/`, `t2/`, `t3/`) untuk skrip Tugas 1–3 dan outputnya, `tree-sitter-filter/` untuk grammar dan highlight Tugas 4–5, `cek/` untuk Tugas 6. Jangan buat folder per mahasiswa.

`git pull` sebelum mulai. Commit per langkah dengan pesan yang menyebut langkahnya, jangan satu commit besar di akhir.

Folder `.venv/` tidak ikut ter-commit, jadi pasang ulang setelah clone.

Versi yang dipakai: Python 3.11, tree-sitter 0.26.1, tree-sitter-python 0.25.0, tree-sitter-javascript 0.25.0.
