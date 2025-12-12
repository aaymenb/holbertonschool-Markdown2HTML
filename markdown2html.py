#!/usr/bin/env python3
import sys
import os
import re

# Fonction pour écrire dans STDERR
def eprint(message):
    sys.stderr.write(message + "\n")

# Fonction principale de conversion
def convert_markdown_to_html(md_file_path, html_file_path):
    """Lit le fichier Markdown, le convertit et écrit le résultat dans le fichier HTML."""
    
    # Ouvrir le fichier de sortie HTML en mode écriture
    try:
        with open(html_file_path, 'w') as html_file:
            
            # Ouvrir le fichier Markdown en mode lecture
            with open(md_file_path, 'r') as md_file:
                in_list = False  # Flag pour suivre si nous sommes à l'intérieur d'une liste (<ul>)
                
                # Lire ligne par ligne
                for line in md_file:
                    line = line.strip()  # Enlever les espaces blancs et sauts de ligne

                    # 1. Traitement des En-têtes (H1 à H6)
                    header_match = re.match(r'^(#{1,6})\s+(.*)$', line)
                    if header_match:
                        level = len(header_match.group(1)) # Nombre de '#' détermine le niveau (1 à 6)
                        content = header_match.group(2)
                        
                        # Si on était dans une liste, on ferme la balise </ul> avant l'en-tête
                        if in_list:
                            html_file.write('</ul>\n')
                            in_list = False
                            
                        html_file.write(f'<h{level}>{content}</h{level}>\n')
                        continue

                    # 2. Traitement des Listes Non Ordonnées
                    list_match = re.match(r'^\*\s+(.*)$', line)
                    if list_match:
                        content = list_match.group(1)
                        
                        # Si ce n'est pas déjà le cas, on ouvre la balise <ul>
                        if not in_list:
                            html_file.write('<ul>\n')
                            in_list = True
                            
                        # Écrire l'élément de liste <li>
                        html_file.write(f'<li>{content}</li>\n')
                        continue
                        
                    # 3. Traitement de la fin de Liste
                    # Si la ligne est vide et qu'on était dans une liste, on ferme la balise </ul>
                    if in_list and not line:
                        html_file.write('</ul>\n')
                        in_list = False
                        continue
                    
                    # 4. Traitement du Texte Normal (non implémenté ici pour la simplicité)
                    if line:
                        # Si on était dans une liste, on la ferme avant d'écrire du texte normal
                        if in_list:
                            html_file.write('</ul>\n')
                            in_list = False
                            
                        # Pour un script de base, nous pouvons simplement écrire la ligne dans un paragraphe
                        # (Bien qu'une gestion complète des paragraphes soit plus complexe en Markdown)
                        html_file.write(f'<p>{line}</p>\n')
                        
                # 5. Gestion de la fin du fichier (si on termine dans une liste ouverte)
                if in_list:
                    html_file.write('</ul>\n')

    except IOError as e:
        eprint(f"Error reading or writing files: {e}")
        sys.exit(1)


# Programme principal (Main)
if __name__ == "__main__":

    # Vérification des Arguments
    if len(sys.argv) < 3:
        eprint("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    md_file = sys.argv[1]       # Fichier Markdown d'entrée
    html_file = sys.argv[2]     # Fichier HTML de sortie

    # Vérification de l'existence du fichier Markdown
    if not os.path.isfile(md_file):
        eprint(f"Missing {md_file}")
        sys.exit(1)
        
    # Exécuter la conversion si les validations réussissent
    convert_markdown_to_html(md_file, html_file)

    # Si tout est bon, quitter avec succès
    sys.exit(0)