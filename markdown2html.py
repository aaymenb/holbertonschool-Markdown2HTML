#!/usr/bin/env python3
import sys
import os

def eprint(msg):
    sys.stderr.write(msg + "\n")

def main():
    if len(sys.argv) < 3:
        eprint("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    md_file = sys.argv[1]
    out_file = sys.argv[2]

    if not os.path.exists(md_file):
        eprint(f"Missing {md_file}")
        sys.exit(1)


    sys.exit(0)

if __name__ == "__main__":
    main()
