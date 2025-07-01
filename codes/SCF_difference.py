from pathlib import Path

file = Path("outputs/SCF_energy.txt")
output_file = Path("outputs/SCF_energy_difference.txt")


def parse_energy(line):
    # this is a helper function to parse the energy from a line
    #it is above the main function so the main function can call it
    parts = line.split()
    filename = parts[0] #name of the file
    energy = float(parts[5]) # energy value
    return filename, energy


def number_difference():
    with open(file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as out:
        for i in range(0, len(lines), 6):
            block = lines[i:i+6]
            # Ensure we have a complete block of 6 lines

            # Parse first line energy
            base_name, base_energy = parse_energy(block[0])

            for line in block:
                name, energy = parse_energy(line)
                diff = energy - base_energy
                out.write(f"{name} difference = {diff * 627.509} Kcal/mol\n")


number_difference()
