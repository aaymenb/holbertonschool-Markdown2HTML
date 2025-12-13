#!/usr/bin/python3
import sys
import os

# Vérifie qu'on a bien 2 arguments (nom du fichier + fichier de sortie)
if len(sys.argv) != 3:
    print(f"Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Vérifie que le fichier Markdown existe
if not os.path.isfile(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# Si tout va bien, on ne fait rien et on sort avec code 0
sys.exit(0) 