#!/usr/bin/python3 
import sys
import os

if __name__ == "__main__":
    # Vérifier le nombre d'arguments
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    md_file = sys.argv[1]
    # Vérifier si le fichier Markdown existe
    if not os.path.isfile(md_file):
        sys.stderr.write(f"Missing {md_file}\n")
        sys.exit(1)

    # Si tout est OK
    sys.exit(0) 