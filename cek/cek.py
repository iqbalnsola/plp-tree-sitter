import sys
from pathlib import Path

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Query, QueryCursor

PY = Language(tspython.language())
parser = Parser(PY)

Q_TODO = Query(PY, '((comment) @c (#match? @c "TODO|FIXME"))')
Q_FUNGSI = Query(PY, "(function_definition name: (identifier) @nama) @fungsi")

def baris_error(node):
    if node.is_error or node.is_missing:
        return node.start_point[0] + 1
    for child in node.children:
        hasil = baris_error(child)
        if hasil:
            return hasil
    return None


def cek_file(path):
    tree = parser.parse(path.read_bytes())

    for node in QueryCursor(Q_TODO).captures(tree.root_node).get("c", []):
        teks = node.text.decode(errors="replace").strip()
        print(f"{path}:{node.start_point[0] + 1}: {teks}")

    for _, cap in QueryCursor(Q_FUNGSI).matches(tree.root_node):
        nama = cap["nama"][0].text.decode(errors="replace")
        fungsi = cap["fungsi"][0]
        jumlah = fungsi.end_point[0] - fungsi.start_point[0] + 1
        if jumlah > 30:
            print(f"{path}:{fungsi.start_point[0] + 1}: fungsi panjang ({jumlah} baris): {nama}")

    if tree.root_node.has_error:
        print(f"{path}:{baris_error(tree.root_node)}: error sintaks pada pohon")


for path in Path(sys.argv[1]).rglob("*.py"):
    cek_file(path)
