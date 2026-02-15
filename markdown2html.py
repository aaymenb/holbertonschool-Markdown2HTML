#!/usr/bin/python3
"""
Markdown to HTML converter module.
This script converts Markdown headings into HTML tags.
"""

import sys
import os


def main():
    """
    Main function to parse arguments and convert markdown headings.
    """
    # 1. Validation des arguments (Check if less than 2 arguments)
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
    try:
        with open(input_file, 'r', encoding='utf-8') as f_in:
            for line in f_in:
                # Analyse de la ligne
                stripped = line.strip()
                if not stripped:
                    continue

                # Comptage des '#'
                h_level = 0
                while h_level < len(stripped) and stripped[h_level] == '#':
                    h_level += 1

                # Validation : 1-6 '#' suivis d'un espace
                if 1 <= h_level <= 6 and len(stripped) > h_level \
                        and stripped[h_level] == ' ':
                            content = stripped[h_level:].strip()
                      tag = f"<h{h_level}>{content}</h{h_level}>\n"
                    html_output.append(tag)

        # 4. Écriture du résultat
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.writelines(html_output)

    except Exception:
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
