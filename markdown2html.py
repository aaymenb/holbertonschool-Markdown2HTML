#!/usr/bin/env python3

import sys
import os

def main():
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    # output_file = sys.argv[2]  # Non utilisé pour la vérification seule

    if not os.path.exists(markdown_file):
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

    # Si les vérifications réussissent, sortir 0
    sys.exit(0)

if __name__ == "__main__":
    main()