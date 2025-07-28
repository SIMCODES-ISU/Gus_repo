import os
from pathlib import Path


def energy_reader(root_directory):
    results = []
    file = Path(root_directory)  # use the passed-in root_directory instead of hardcoding

    for files in file.iterdir():  # iterate
        if files.name.endswith(".out"):
            file_path = files  # get the full path of the files that end with .out

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
                            total_time = words[3]
                        except IndexError:
                            total_time = None
                        # Extract the total time from the line, and if it fails, set it to None

                filename = files.name  # define filename here for use below
                if energy_value is not None and total_time is not None:
                    results.append((filename, energy_value, total_time))
                    # if both energy and time are found, append them to the results, if not, append None
                else:
                    results.append((filename, None, None))

    results.sort(key=lambda x: x[0])
    # sort on the first element of the tuple, which is the filename

    output_path = Path("energy_reader/energies/SCF_energy.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # path to the output file, create the directory if it does not exist
    with open(output_path, 'w') as w:
        w.write("Filename                            (Hartrees)         (Seconds)\n")
        # write the header to the file
        for filename, energy, total_time in results:
            if energy is not None and total_time is not None:
                # if both energy and time are not None, write them to the file
                w.write(f"{filename} Total SCF energy = {energy} in {total_time}\n")
            else:
                w.write(f"{filename} NO DATA HERE\n")
                # if either energy or time is None, write NO DATA HERE to the file


def path():
    dir_path = Path("energy_reader/inputs")  # make this match your actual inputs directory
    return dir_path
# give the function a path of the .out files


energy_reader(path())
