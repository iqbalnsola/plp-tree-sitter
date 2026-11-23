# cek.py

CLI kecil untuk memeriksa folder berisi berkas Python memakai tree-sitter. Hasilnya tiga laporan:

1. Komentar yang memuat `TODO` atau `FIXME`, beserta berkas dan barisnya.
2. Fungsi yang badannya lebih dari 30 baris.
3. Berkas yang pohon sintaksnya mengandung error, beserta baris pertama yang bermasalah.

## Pasang

```bash
pip install tree-sitter tree-sitter-python
```

Versi yang dipakai: Python 3.11, tree-sitter 0.26.1, tree-sitter-python 0.25.0.

## Jalankan

```bash
python cek.py <folder>
```

Contoh:

```bash
python cek.py uji
python cek.py C:/path/ke/repo_python
```

## Contoh output

Pada folder `uji/` berisi tiga berkas uji buatan sendiri:

```
uji\ber_todo.py:2: # TODO: tangani nilai negatif
uji\fungsi_panjang.py:1: fungsi panjang (37 baris): hitung_laporan
uji\sintaks_rusak.py:2: error sintaks pada pohon
```

Pada repositori nyata `itsdangerous` (15 berkas Python, hasil lengkap di `out/repo_nyata.txt`):

```
...\itsdangerous\signer.py:182: fungsi panjang (32 baris): derive_key
...\itsdangerous\timed.py:182: # TODO: Signature is incompatible because parameters were added
...\itsdangerous\timed.py:72: fungsi panjang (87 baris): unsign
...\itsdangerous\url_safe.py:23: fungsi panjang (31 baris): load_payload
```

Angka pada `timed.py` dan `url_safe.py` sudah dicocokkan dengan modul `ast` bawaan Python sebagai pembanding independen, dan hasilnya sama.

## Batasan

- Semua `function_definition` dihitung, termasuk method di dalam kelas dan fungsi bersarang. Fungsi bersarang juga dilaporkan terpisah dari fungsi induknya.
- `#match? "TODO|FIXME"` bersifat case-sensitive, jadi komentar `# todo:` dengan huruf kecil tidak terdeteksi.
- Kesalahan indentasi tidak terdeteksi: grammar Python tetap menghasilkan pohon tanpa `ERROR`, sehingga `has_error` bernilai `False`.
- Baris yang dilaporkan untuk error adalah node bermasalah pertama yang ditemukan parser, bukan selalu baris yang akan ditunjuk manusia. Contoh: `return (a + b` yang kekurangan kurung tutup dilaporkan di baris 2, bukan baris 1.
- Folder `.git`, `.venv`, `venv`, `node_modules`, `__pycache__`, `build`, dan `dist` dilewati.
