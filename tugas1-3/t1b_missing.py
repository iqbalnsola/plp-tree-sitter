import tree_sitter_javascript as tsjs
from tree_sitter import Language, Parser

parser = Parser(Language(tsjs.language()))

kode = b"let nilai = (1 + 2;\n"
tree = parser.parse(kode)
print(tree.root_node)


def cari_rusak(node, kedalaman=0):
    if node.is_error or node.is_missing:
        jenis = "MISSING" if node.is_missing else "ERROR"
        baris, kolom = node.start_point
        print("  " * kedalaman + f"{jenis} {node.type} [{baris + 1}:{kolom}]")
    for child in node.children:
        cari_rusak(child, kedalaman + 1)


cari_rusak(tree.root_node)
