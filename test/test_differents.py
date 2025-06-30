from pathlib import Path

file_path = Path(__file__).parent.parent / "outputs" / "energy_difference.txt"


def test_all_number_graber():
    with open(file_path, 'r') as f:
        for index, line in enumerate(f):
            word = line.split()
            if index == 0:
                assert (word[3]) == "0.0"
            elif index == 1:
                assert (word[3]) == "0.0009947989739202967"
            elif index == 2:
                assert (word[3]) == "-0.001010732101008216"
            elif index == 3:
                assert (word[3]) == "-0.0019948966190668216"
            elif index == 4:
                assert (word[3]) == "0.0035428792299398992"
            elif index == 5:
                assert (word[3]) == "0.0037509549539436193"


test_all_number_graber()


#     with open(file, 'r') as f:
#         for index, line in enumerate(f):
#             word = line.split()
#             if (index + 1) % 6 > 0:
#                 every_sixth_line.append((index, word[0], float(word[5])))
#                 print(index)

#     return every_sixth_line


# print(all_number_graber())
