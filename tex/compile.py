#!/usr/bin/env python3

import subprocess, sys, os


def compile(filename):
    commands = [
        ["pdflatex", "-halt-on-error", sys.argv[1] + ".tex"],
        ["bibtex", "-terse", sys.argv[1] + ".aux"],
        ["pdflatex", "-halt-on-error", sys.argv[1] + ".tex"],
        ["pdflatex", "-halt-on-error", sys.argv[1] + ".tex"],
    ]

    for cmd in commands:
        null = open("/dev/null")
        # subprocess.run(cmd, stderr=null, stdout=null)
        subprocess.run(cmd)
        null.close()

    clean()


def clean():
    cleanFiles = [
        "blx.bib",
        ".run.xml",
        ".aux",
        ".bbl",
        ".bcf",
        ".blg",
        ".idx",
        ".ind",
        ".lof",
        ".lot",
        ".out",
        ".toc",
        ".acn",
        ".acr",
        ".alg",
        ".glg",
        ".glo",
        ".gls",
        ".ist",
        ".fls",
        ".log",
        ".fdb_latexmk",
        ".snm",
        ".nav",
    ]
    to_remove = [file for file in os.listdir(os.curdir) for ext in cleanFiles if file.endswith(ext)]
    for file in to_remove:
        os.remove(file)
        

if __name__ == "__main__":
    operationNotSupplied = False

    try:
        operation = sys.argv[1]
        if operation not in ["compile", "clean"]:
            raise IndexError
    except IndexError:
        operation = "compile"
        operationNotSupplied = True

    match operation:
        case "compile":
            file = None
            try:
                file = sys.argv[2 if not operationNotSupplied else 1]
            except IndexError:
                print(f"file not supplied")
                exit()

            print(f"compiling {file}")
            compile(file)
        case "clean":
            print("clean option selected")
            clean()
