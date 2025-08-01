from pathlib import Path

file = Path("energy_reader/energies/SCF_energy.txt")
output_file = Path("energy_reader/energies/SCF_energy_difference.txt")
#file paths

def parse_energy(line):
    parts = line.split()
    filename = parts[0]  # name of the file
    # Check if line contains energy value or "NO DATA HERE"
    if "NO DATA HERE" in line:
        return filename, None
    # if it does not contain energy value, return None
    try:
        energy = float(parts[5])  # energy value
        return filename, energy
    except (IndexError, ValueError):
        return filename, None
    # if it fails to parse the energy value, return None


def number_difference():
    with open(file, 'r') as f:
        lines = f.readlines()

    lines = lines[1:]
    # skip the first line if it is a header or not needed
    with open(output_file, 'w') as out:
        out.write("Filename Difference        (Kcal/mol)\n")
        # process lines in blocks of 6 (assuming grouped data)
        for i in range(0, len(lines), 6):
            block = lines[i:i+6]

            # parse the base energy (first line with valid energy)
            base_energy = None
            base_name = None
            for line in block:
                name, energy = parse_energy(line)
                if energy is not None:
                    base_energy = energy
                    base_name = name
                    break

            if base_energy is None:
                # no valid energy in block, write a message or skip
                out.write(
                    f"Block starting with {block[0].split()[0]} has no valid energy data.\n")
                continue

            # calculate and write differences for the block
            for line in block:
                name, energy = parse_energy(line)
                if energy is not None:
                    # convert Hartree to Kcal/mol
                    diff = (energy - base_energy) * 627.509
                    out.write(f"{name} difference = {diff:.6f}\n")
                else:
                    out.write(f"{name} difference = NO DATA\n")
                    # difference and write NO DATA if energy is None


number_difference()
