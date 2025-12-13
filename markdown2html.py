#!/usr/bin/python3
import sys
from os import path

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    if not path.exists(sys.argv[1]):
        print(f"Missing {sys.argv[1]}", file=sys.stderr)
        sys.exit(1)

    with open(sys.argv[1], "r") as md, open(sys.argv[2], "w") as html:
        for line in md:
            line = line.rstrip("\n")

            count = 0
            for c in line:
                if c == "#":
                    count += 1
                else:
                    break

            if count > 0 and count <= 6 and line[count] == " ":
                content = line[count+1:]
                html.write(f"<h{count}>{content}</h{count}>\n")
