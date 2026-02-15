#!/usr/bin/python3
"""
Markdown to HTML converter.
This script parses Markdown headings (# to ######) into HTML tags.
"""

import sys
import os


def main():
    """
    Main entry point for the markdown2html script.
    Checks arguments, validates file existence, and parses headings.
    """
    # 1. Validation des arguments
    if len(sys.argv) < 3:
        usage = "Usage: ./markdown2html.py README.md README.html"
        print(usage, file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # 2. Vérification de l'existence du fichier
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # 3. Lecture et conversion
    html_output = []
    with open(input_file, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            # Nettoyage de la ligne (enlever les espaces de fin)
            clean_line = line.strip()
            if not clean_line:
                continue

            # Comptage des '#' au début
            count = 0
            while count < len(clean_line) and clean_line[count] == '#':
                count += 1

            # Si c'est un titre (1-6 '#' suivis d'un espace)
            if 1 <= count <= 6 and len(clean_line) > count and \
                    clean_line[count] == ' ':
                        content = clean_line[count:].strip()
                html_output.append(f"<h{count}>{content}</h{count}>\n")

    # 4. Écriture du résultat
    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.writelines(html_output)

    sys.exit(0)


if __name__ == "__main__":
    main()
