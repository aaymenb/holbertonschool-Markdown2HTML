#!/usr/bin/env python3
import sys
import os

# Fonction pour écrire dans STDERR
def eprint(message):
    sys.stderr.write(message + "\n")

# Programme principal
if __name__ == "__main__":

    # Vérifier si on a au moins 2 arguments
    if len(sys.argv) < 3:
        eprint("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    md_file = sys.argv[1]      # 1er argument = fichier markdown
    html_file = sys.argv[2]    # 2e argument = fichier sortie

    # Vérifier si le fichier markdown existe
    if not os.path.isfile(md_file):
        eprint(f"Missing {md_file}")
        sys.exit(1)

    # Si tout est bon : rien afficher
    sys.exit(0)
