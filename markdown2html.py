#!/usr/bin/python3
"""
Script pour convertir du Markdown en HTML.
Gère maintenant la conversion des titres (Headings) de 1 à 6.
"""

import sys
import os


def main():
    """
    Fonction principale qui valide les arguments et convertit
    les titres Markdown en balises HTML.
    """
    # 1. Validation des arguments
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # 2. Vérification de l'existence du fichier
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # 3. Lecture et conversion
    try:
        with open(input_file, 'r', encoding='utf-8') as f_in:
            lines = f_in.readlines()

        html_output = []
        for line in lines:
            # On compte le nombre de '#' au début de la ligne
            stripped_line = line.lstrip()
            count = 0
            while count < len(stripped_line) and stripped_line[count] == '#':
                count += 1

            # Si on a entre 1 et 6 '#' suivis d'un espace
            if 1 <= count <= 6 and len(stripped_line) > count and \
                    stripped_line[count] == ' ':
                        content = stripped_line[count:].strip()
                html_output.append(f"<h{count}>{content}</h{count}>\n")
            else:
                # Pour l'instant, on ignore ce qui n'est pas un titre
                # ou on l'ajoute tel quel si nécessaire
                pass

        # 4. Écriture du résultat
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.writelines(html_output)

    except Exception:
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
