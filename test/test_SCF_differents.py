from pathlib import Path

file_path = Path(__file__).parent.parent / "outputs" / \
    "SCF_energy_difference.txt"
#file path

def test_all_number_graber():
    # Check if file exists
    assert file_path.exists(), f"File {file_path} does not exist."

    # Expected difference values for first 6 lines (index 0 to 5)
    expected_differences = [
        0.000000,
        0.624245,
        -0.634243,
        -1.251816,
        2.223189,
        2.353758
    ]

    with open(file_path, 'r') as f:
        header = f.readline()  # skip header line
        for index, line in enumerate(f):
            if index >= len(expected_differences):
                break  # only check first 6 lines

            word = line.strip().split()
            # Extract the difference string and convert to float
            diff_value = float(word[3])

            # Assert approximate equality with tolerance
            assert abs(diff_value - expected_differences[index]) < 1e-6, (
                f"Line {index+2}: expected {expected_differences[index]}, got {diff_value}"
            )


test_all_number_graber()
