"""Tugas 2: penjelajah node. Versi rekursif (named_children) dan versi TreeCursor."""
import sys
import tree_sitter_python as tspython
from tree_sitter import Language, Parser

parser = Parser(Language(tspython.language()))


def jelajah(node, kedalaman=0, field=None):
    baris, kolom = node.start_point
    label = f"{field}: " if field else ""
    print("  " * kedalaman + f"{label}{node.type} [{baris + 1}:{kolom}]")
    # enumerate atas SEMUA child (node.children) supaya indeks cocok dengan
    # field_name_for_child(i); node anonim dilewati.
    for i, child in enumerate(node.children):
        if not child.is_named:
            continue
        jelajah(child, kedalaman + 1, node.field_name_for_child(i))


def jelajah_cursor(tree):
    """Versi pengayaan memakai TreeCursor, output harus identik dengan jelajah()."""
    cursor = tree.walk()
    kedalaman = 0
    while True:
        node = cursor.node
        if node.is_named:
            baris, kolom = node.start_point
            fld = cursor.field_name
            label = f"{fld}: " if fld else ""
            print("  " * kedalaman + f"{label}{node.type} [{baris + 1}:{kolom}]")
            if cursor.goto_first_child():
                kedalaman += 1
                continue
        while not cursor.goto_next_sibling():
            if not cursor.goto_parent():
                return
            kedalaman -= 1


if __name__ == "__main__":
    with open(sys.argv[1], "rb") as f:
        tree = parser.parse(f.read())
    if len(sys.argv) > 2 and sys.argv[2] == "--cursor":
        jelajah_cursor(tree)
    else:
        jelajah(tree.root_node)