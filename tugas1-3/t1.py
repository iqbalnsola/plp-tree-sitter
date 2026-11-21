import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))

POTONGAN = {
    "fungsi": b"def hitung_luas(panjang, lebar):\n    return panjang * lebar\n",
    "if_else": b'if nilai >= 75:\n    print("lulus")\nelse:\n    print("belum lulus")\n',
    "kelas": b"class Akun:\n    def __init__(self, nama):\n        self.nama = nama\n",
    "rusak_kolom": b"def sapa(nama)\n    return nama\n",
    "rusak_kurung": b"def sapa(nama:\n    return nama\n",
}

for nama, kode in POTONGAN.items():
    tree = parser.parse(kode)
    print(f"--- {nama} ---")
    print(tree.root_node)
    print()

print("--- anak-anak function_definition (bernama vs anonim) ---")
tree = parser.parse(POTONGAN["fungsi"])
fungsi = tree.root_node.children[0]
for c in fungsi.children:
    print(c.type, "bernama" if c.is_named else "anonim")

print()
print("--- anak-anak node parameters ---")
params = fungsi.child_by_field_name("parameters")
for c in params.children:
    print(c.type, "bernama" if c.is_named else "anonim")

print()
print("--- node rusak: ERROR dan MISSING ---")


def cari_rusak(node, kedalaman=0):
    if node.is_error or node.is_missing:
        jenis = "MISSING" if node.is_missing else "ERROR"
        baris, kolom = node.start_point
        print("  " * kedalaman + f"{jenis} {node.type} [{baris + 1}:{kolom}]")
    for child in node.children:
        cari_rusak(child, kedalaman + 1)


tree_rusak = parser.parse(POTONGAN["rusak_kolom"])
print("tanpa titik dua:")
print(tree_rusak.root_node)
cari_rusak(tree_rusak.root_node)

tree_rusak2 = parser.parse(POTONGAN["rusak_kurung"])
print()
print("tanpa tanda tutup kurung:")
print(tree_rusak2.root_node)
cari_rusak(tree_rusak2.root_node)
