from pathlib import Path


def get_xyz_files():
    directory = Path(__file__).resolve().parent
    return list(directory.rglob("*.xyz"))


def xyz_to_nw(xyz_path, output_dir):
    output_file = output_dir / (xyz_path.stem + ".nw")

    with open(xyz_path, 'r') as g:
        lines = g.readlines()

    with open(output_file, 'w') as f:
        f.write(f"start {xyz_path.stem}\n")
        f.write("geometry\n")
        for line in lines:
            if len(line.strip().split()) == 4:
                f.write(line.strip() + "\n")
        f.write("end\n\n")

        f.write("basis\n")
        f.write(" * library aug-cc-pvdz\n")
        f.write("end\n\n")

        f.write("echo\n\n")
        
        f.write("scf\n")
        f.write(" direct\n")
        f.write("end\n\n")
        
        f.write("task scf energy\n")



def batch_write_files_to_desktop():
  
    desktop = Path.home() / "Desktop"
    output_dir = desktop / "nwchem_inputs"
    output_dir.mkdir(exist_ok=True)

    xyz_files = get_xyz_files()
    for xyz_file in xyz_files:
        xyz_to_nw(xyz_file, output_dir)


batch_write_files_to_desktop()
