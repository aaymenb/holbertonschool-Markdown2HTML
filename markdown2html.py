#!/usr/bin/env python3
import sys
import os

# Vérifie le nombre d'arguments
if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Vérifie si le fichier Markdown existe
if not os.path.exists(input_file):
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

# Si tout va bien
sys.exit(0) 