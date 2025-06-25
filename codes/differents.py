from pathlib import Path

file = Path("outputs/energy.txt")
output_file = Path("outputs/energy_difference.txt")


def all_number_graber():
    number = []
    with open(file, 'r') as f:
        for line in f:
            word = line.split()
            if len(word) > 5:
                number.append((word[0], float(word[5])))
    return number


# print(all_number_graber())


def first_number_graber():
    with open(file, 'r') as d:
        line = d.readline()
        words = line.split()
        return float(words[5])


# print(first_number_graber())

def number_difference():
    a = (all_number_graber())
    f = (first_number_graber())

    with open(output_file, 'w') as out:
        for name, value in a:
            diff = value - f
            out.write(f"{name} difference = {diff}\n")

    print(f" Saved {len(a)} difference to {output_file}")


number_difference()
