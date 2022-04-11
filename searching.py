import json
import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field in set(data.keys()):
        return data[field]


def linear_search(sequence, searched_number):
    positions = []
    count = 0

    for i, number in enumerate(sequence):
        if number == searched_number:
            count += 1
            positions.append(i)

    output = dict()
    output["positions"] = positions
    output["count"] = count
    return output


def pattern_search(sequence, pattern):

    dna_segmented = []
    segment_range = []
    start_index = 0
    zoznam = []

    for index in range(len(sequence) - len(pattern) - 1):
        if sequence[index:index + len(pattern)] != pattern:
            continue
        else:
            dna_segmented.append(sequence[start_index:index])
            segment_range.append([start_index, index - 1])
            start_index = index + len(pattern)
            zoznam.append(index)

    return set(zoznam)


def main():
    unordered_numbers = read_data("sequential.json", "unordered_numbers")
    data = read_data("sequential.json", "dna_sequence")
    print(pattern_search(data, "ATA"))


if __name__ == '__main__':
    main()