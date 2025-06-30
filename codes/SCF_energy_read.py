import os
from pathlib import Path


def energy_reader(root_directory):
    results = []
    for root, dirs, files in os.walk(root_directory):
        for filename in files:
            if filename.endswith(".out"):
                file_path = os.path.join(root, filename)

                energy_value = None
                total_time = None

                with open(file_path, 'r') as f:
                    for line in f:
                        if "Total SCF energy" in line:
                            words = line.split()
                            energy_value = float(words[4])
                        if "Total times" in line:
                            words = line.split()
                            total_time = (words[3])
                    if energy_value is not None and total_time is not None:
                        results.append((filename, energy_value, total_time))

    results.sort(key=lambda x: x[0])

    output_path = Path("outputs/energy.txt")

    with open(output_path, 'w') as w:
        for filename, energy, total_time in results:
            w.write(f"{filename} Total SCF energy = {energy} in {total_time}\n")


def path():
    dir_path = Path("read")
    return dir_path


(energy_reader(path()))
