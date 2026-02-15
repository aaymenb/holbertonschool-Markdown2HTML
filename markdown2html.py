#!/usr/bin/python3
"""
A script that takes two arguments: 
1. The name of the Markdown file
2. The output file name
"""

import sys
import os

def main():
    # Check if the number of arguments is less than 2
    # sys.argv[0] is the script name, so we need 3 total elements
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check if the Markdown file exists
    if not os.path.isfile(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # If requirements are met, exit 0
    sys.exit(0)

if __name__ == "__main__":
    main()
