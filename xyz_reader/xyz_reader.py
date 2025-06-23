from pathlib import Path


def water_path():
    return Path(__file__).resolve().parent / "file.xyz"


def write_file():
    geometry_file = water_path()
    output_file = geometry_file.with_name("nwchem.xyz")

    with open(geometry_file, 'r') as g:
        lines = g.readlines()

    with open(output_file, 'w') as f:
        f.write("start test\n")
        f.write("gemetry\n")
        for line in lines:
            if len(line.strip().split()) == 4:
                f.write(line.strip() + "\n")
        f.write("end\n")
        f.write("\n")

        f.write("basis\n")
        f.write(" * library aug-cc-pvdz\n")
        f.write("end\n")
        f.write("\n")

        f.write("task scf energy")


write_file()
