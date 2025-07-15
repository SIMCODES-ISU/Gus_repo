import os
from pathlib import Path


def energy_reader(root_directory):
    results = []
    for root, dirs, files in os.walk(root_directory):
        for filename in files:
            if filename.endswith(".out"):
                file_path = os.path.join(root, filename)
                # read all files ends with .out in the directory

                energy_value = None
                total_time = None

                with open(file_path, 'r') as f:
                    for line in f:
                        if "Total SCF energy" in line:
                            words = line.split()
                            try:
                                energy_value = float(words[4])
                            except (IndexError, ValueError):
                                energy_value = None
                            # Extract the energy value from the line, and if it fails, set it to None
                        if "Total times" in line:
                            words = line.split()
                            try:
                                total_time = (words[3])
                            except IndexError:
                                total_time = None
                            # Extract the total time from the line, and if it fails, set it to None
                    if energy_value is not None and total_time is not None:
                        results.append((filename, energy_value, total_time))
                    else:
                        results.append((filename, None, None))

    results.sort(key=lambda x: x[0])
    # sort on the fist element of the tuple, which is the filename

    output_path = Path("outputs/SCF_energy.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w') as w:
        w.write("Filename                            (Kcal/mol)         (Seconds)\n")
        for filename, energy, total_time in results:
            if energy is not None and total_time is not None:
                w.write(
                    f"{filename} Total SCF energy = {energy} in {total_time}\n")
            else:
                w.write(f"{filename} NO DATA HERE\n")


def path():
    dir_path = Path("read")
    return dir_path
# give the function a path of the .out files


energy_reader(path())
