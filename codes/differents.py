from pathlib import Path

file = Path("outputs/energy.txt")
output_file = Path("outputs/energy_difference.txt")


def parse_energy(line):
    # Extract filename and energy float from a line like:
    # ALA_ALA_0.out Total SCF energy = -699.782153441754
    parts = line.split()
    filename = parts[0] #name
    energy = float(parts[5]) # energy value
    return filename, energy


def number_difference():
    with open(file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as out:
        for i in range(0, len(lines), 6):
            block = lines[i:i+6]

            # Parse first line energy
            base_name, base_energy = parse_energy(block[0])

            for line in block:
                name, energy = parse_energy(line)
                diff = energy - base_energy
                out.write(f"{name} difference = {diff}\n")


number_difference()
