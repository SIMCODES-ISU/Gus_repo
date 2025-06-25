import os
from pathlib import Path


def energy(root_directory):
    results = []
    for root, dirs, files in os.walk(root_directory):
        for filename in files:
            if filename.endswith(".out"):
                file_path = os.path.join(root, filename)

                with open(file_path, 'r') as f:
                    for line in f:
                        if "Total SCF energy" in line:
                            words = line.split()
                            energy_value = float(words[4])
                            results.append(
                                (filename, energy_value))
                            break

    results.sort(key=lambda x: x[0])

    output_path = Path("outputs/energy.txt")

    with open(output_path, 'w') as w:
        for filename, energy in results:
            w.write(f"{filename} Total SCF energy = {energy}\n")


def path():
    dir_path = Path("read")
    return dir_path


energy(path())
