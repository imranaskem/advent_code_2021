import csv
import os


def load_text_file(name, filepath, process):
    inputs = []

    path = get_file_path(name, filepath)

    with open(path) as file:
        for line in file:
            inputs.append(process(line))

    return inputs


def load_text_file_get_num_list(name, filepath):
    inputs = []

    path = get_file_path(name, filepath)

    with open(path) as file:
        for line in file:
            inputs.append(int(line))

    return inputs


def load_csv_file_get_num_list(filename, executingfilepath):
    path = get_file_path(filename, executingfilepath)

    results = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:  # each row is a list
            for num in row:
                results.append(int(num))

    return results


def load_csv_file_get_instructions(filename, executingfilepath):
    path = get_file_path(filename, executingfilepath)

    results = []

    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:  # each row is a list
            results.append([instruc for instruc in row])

    return results


def get_file_path(filename, executingfilepath):
    dirname = os.path.dirname(executingfilepath)
    path = os.path.join(dirname, filename)

    return path
