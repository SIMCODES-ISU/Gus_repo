from pathlib import Path
# import path


def h2_file_path():
    return Path(__file__).resolve().parent / "h2_output.txt"
# path of file


def read(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if "Total SCF energy" in line:
                words = line.split()
                print("SCF energy =", words[4])


read(h2_file_path())
