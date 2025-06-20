from pathlib import Path
# import path


def h2_file_path():
    project_root = Path(__file__).resolve().parent.parent
    return project_root / "output" / "h2_output.txt"
# path of file


def read(file):
    with open(file, 'r') as f:
        lines = f.readlines()
# Read all lines into a list
        for i, line in enumerate(lines):
            if line.split().startswith("Total SCF energy"):
                print(line)


read(h2_file_path())

# /Users/guswoodard/Desktop/simcodes/Gus_h2_reader-1/h2/h2_output.txt