from pathlib import Path


def get_out_files():
    directory = Path(__file__).resolve().parent.parent / "inputs"
    return list(directory.rglob("*.out"))
# file path


def get_atomic_info(file_path, output_dir):
    output_file = output_dir / (file_path.stem + ".txt")
# .out to .txt file
    lines_in_section = []
    in_line = False
    blank_count = 0

    with open(file_path, 'r') as f:
        for line in f:
            if "Mulliken analysis of the total density" in line:
                in_line = True
                lines_in_section.append(line.strip())
                continue
# ckeck for Mulliken analysis section
            if in_line:
                if line.strip() == "":
                    blank_count += 1
                    if blank_count == 2:
                        break
                    continue
                lines_in_section.append(line.strip())
                blank_count = 0
# get all the desired information from the section
    if lines_in_section:
        with open(output_file, 'w') as f_out:
            for line in lines_in_section:
                f_out.write(line + "\n")
        return True
    else:
        return False
# if the section is found, write it to the output file and return True, otherwise return False


def write():
    output_dir = Path("energy_reader/atomic_info")
    output_dir.mkdir(parents=True, exist_ok=True)
# output dir path and create it if it doesn't exist
    missing_file_log = output_dir / "_no_info.txt"
    missing_files = []
# files that do not have the desired information
    out_files = get_out_files()
    for out_file in out_files:
        found = get_atomic_info(out_file, output_dir)
        if not found:
            missing_files.append(out_file.name)
# if the section is not found, add the file name to the missing_files list

    if missing_files:
        with open(missing_file_log, 'w') as f:
            f.write("Files that do not have the information:\n")
            for name in missing_files:
                f.write(name + "\n")
# write the files that do not hvae the desired information to a log file


write()
#run the write function to execute the code
