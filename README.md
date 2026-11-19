# Tugas 1: Membaca Pohon Tree-sitter

Tugas 1 praktikum PLP. Parse potongan kode Python pakai tree-sitter, lalu baca pohon yang dihasilkan.

## Cara jalan

```bash
git clone https://github.com/iqbalnsola/plp-tree-sitter.git
cd plp-tree-sitter
uv venv .venv
uv pip install --python .venv/Scripts/python.exe tree-sitter tree-sitter-python tree-sitter-javascript
.venv/Scripts/python.exe t1.py
```

Di Windows bisa juga dobel klik `run.bat`.

Kalau tidak pakai `uv`, ganti dua baris tengahnya dengan:

```bash
python -m venv .venv
.venv/Scripts/pip install tree-sitter tree-sitter-python tree-sitter-javascript
```

## Isi folder

`t1.py`
Parse tiga potongan kode (fungsi, if/else, kelas) dan cetak pohonnya. Lalu cetak anak-anak node `function_definition` dan `parameters` untuk membedakan node bernama dan anonim. Terakhir parse dua kode yang sengaja dirusak.

`t1b_missing.py`
Kode JavaScript yang kurung tutupnya hilang. Ini yang memunculkan node `MISSING`.

`pohon-perkiraan.txt`
Pohon yang saya tulis sebelum skrip dijalankan, termasuk dua tebakan yang ternyata salah.

`out/`
Hasil run, disimpan sebagai bukti.

## Yang perlu diperhatikan di output

Node anonim tidak ikut tercetak di S-expression. `def`, titik dua, `(`, `)`, dan `,` tetap ada di pohon, tapi hanya kelihatan kalau dicetak lewat `children` dan `is_named`. Ini juga beda antara `children` (semua anak) dan `named_children` (hanya yang bernama, dan itulah yang tampil di S-expression).

Dua tebakan awal saya salah. `panjang * lebar` ternyata `binary_operator` dengan field `left` dan `right`, bukan satu node biasa. `self.nama` ternyata `attribute` yang berisi `object` dan `attribute`, bukan `identifier`.

Soal node rusak: menghapus `:` atau `)` di Python sama-sama menghasilkan `ERROR`, bukan `MISSING`. `MISSING` baru muncul di grammar JavaScript, terlihat di `t1b_missing.py` sebagai `MISSING ")"` pada 1:18. Jadi keberadaan keduanya bergantung pada grammar yang dipakai.

## Pembagian kerja

Tugas 1 dikerjakan Muhammad Iqbal (`iqbalnsola`) dan ada di root folder. Tugas berikutnya taruh di folder sendiri (`tugas2/`, `tugas3/`, dst) supaya tidak bentrok. `git pull` sebelum mulai, commit per langkah dengan pesan yang menyebut langkahnya, jangan satu commit besar di akhir.

Folder `.venv/` tidak ikut ter-commit, jadi pasang ulang setelah clone.

Versi yang dipakai: Python 3.11, tree-sitter 0.26.1, tree-sitter-python 0.25.0, tree-sitter-javascript 0.25.0.
