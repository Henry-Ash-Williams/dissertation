#!/usr/bin/env python3

import subprocess, sys, os
from subprocess import CalledProcessError

def help():
    print("""compile.py: A simple python tool to make compiling LaTeX projects easier
USAGE: ./compile.py [options] [filename]

OPTIONS:
    compile [filename]      Compile the LaTeX document
    clean                   Remove all compilation artifacts from the current working directory
    help | --help | -h      Show this message

NOTE:
    This program expects filenames to be provided WITHOUT an extension.

EXAMPLES:
    Compile the document named 'main.tex'
    $ ./compile.py compile main

    Clean the current working directory, removes all compiler artefacts
    $ ./compile.py clean

    Show this message
    $ ./compile.py help
    $ ./compile.py --help
    $ ./compile.py -h""")

def compile(filename):
    commands = [
        ["pdflatex", "-halt-on-error", filename + ".tex"],
        ["bibtex", "-terse", filename + ".aux"],
        ["pdflatex", "-halt-on-error", filename + ".tex"],
    ]

    for cmd in commands:
        completed_process = subprocess.run(cmd)
        try:
            completed_process.check_returncode()
        except CalledProcessError:
            print(f"ERROR: Command {cmd} failed")


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
        ".gz",
    ]
    to_remove = [file for file in os.listdir(os.curdir) for ext in cleanFiles if file.endswith(ext)]
    for file in to_remove:
        os.remove(file)


if __name__ == "__main__":
    if int(sys.version[1]) < 10:
        print("ERROR: This program requires Python version 3.10 and above")
        exit()

    try:
        operation = sys.argv[1]
    except IndexError:
        help()
        exit()

    match operation:
        case "compile":
            file = None
            try:
                file = sys.argv[2]
            except IndexError:
                print("ERROR: Expected a filename")
                exit()

            print(f"compiling {file}")
            if not os.path.exists(f"{file}.tex"):
                print(f"ERROR: {file}.tex not found")
                exit()
            compile(file)
        case "clean":
            clean()
        case "--help" | "-h" | "help":
            help()
        case _:
            help()
