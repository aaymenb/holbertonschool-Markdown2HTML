#!/usr/bin/python3
"""
Sujet : Script pour convertir du Markdown en HTML.
Ce module vérifie les arguments et l'existence du fichier source.
"""

import sys
import os


def main():
    """
    Fonction principale qui gère la validation des arguments
    et l'existence du fichier d'entrée.
    """
    # Vérifie si le nombre d'arguments est inférieur à 2 (script + 2 args)
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]

    # Vérifie si le fichier Markdown existe
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Si tout est OK, on sort avec 0
    sys.exit(0)


if __name__ == "__main__":
    main()
