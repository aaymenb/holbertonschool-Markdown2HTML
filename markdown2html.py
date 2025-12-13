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

# Lecture du fichier Markdown
with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

html_lines = []

for line in lines:
    line = line.rstrip()  # Supprime le \n
    if line.startswith("#"):  # Vérifie si c'est un heading
        # Compte le nombre de # au début
        count = 0
        while count < len(line) and line[count] == "#":
            count += 1
        if count > 6:  # On limite à h6 max
            count = 6
        content = line[count:].strip()  # Texte après les #
        html_lines.append(f"<h{count}>{content}</h{count}>")
    else:
        # On ignore les autres lignes pour l'instant
        pass

# Écriture du fichier HTML
with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n".join(html_lines))
