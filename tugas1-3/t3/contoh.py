"""Modul contoh untuk latihan query Tugas 3."""

import os
from pathlib import Path


def sapa(nama):
    """Sapa satu orang."""
    print("Halo,", nama)


def tambah(a, b):
    return a + b


def cetak_hasil(nilai, label, satuan):
    print(label, nilai, satuan)


class Penghitung:
    def __init__(self, awal):
        self.awal = awal

    def tambah_satu(self):
        self.awal = self.awal + 1
        return self.awal


def main():
    sapa("Iqbal")
    print(tambah(2, 3))
    cetak_hasil(10, "suhu", "C")


if __name__ == "__main__":
    main()
