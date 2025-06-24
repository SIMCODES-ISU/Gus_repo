import os
from pathlib import Path


def lol(root_directory):
    for root, dirs, files in os.walk(root_directory):
        for filename in files:
            if filename.endswith(".out"):
                file_path = os.path.join(root, filename)

                with open(file_path, 'r') as f:
                    lines = f.readlines()

                output_filename = "energy.txt"
                output_path = os.path.join(root, output_filename)

                with open(output_path, 'a') as w:
                    for line in lines:
                        if "Total SCF energy" in line:
                            words = line.split()
                            w.write(filename)
                            w.write(" Total SCF energy = ")
                            w.write(words[4])
                            w.write("\n")


def path():
    dir_path = Path("h2")
    return dir_path


lol(path())
