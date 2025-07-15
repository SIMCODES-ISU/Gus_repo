import pytest
from pathlib import Path

file_path = Path(__file__).parent.parent / "outputs" / "SCF_energy.txt"


def test_energy_value_in_second_line():
    assert file_path.exists(), f"File {file_path} does not exist."

    with open(file_path, 'r') as f:
        header = f.readline()
        second_line = f.readline().strip().split()
        energy = float(second_line[5])

    expected_energy = -699.782153441754
    tolerance = 1e-9
    assert abs(
        energy - expected_energy) < tolerance, f"Energy {energy} differs from expected {expected_energy}"
