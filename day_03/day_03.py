from utils.utils import load_text_file


def calculate_rates(binaries: list) -> int:
    threshold = len(binaries) // 2
    binary_length = len(binaries[0]) - 1
    gamma, epsilon = '', ''
    for i in range(0, binary_length):
        if sum([1 for bin in binaries if bin[i] == '1']) > threshold:
            gamma += '1'
        else:
            gamma += '0'
    for char in gamma:
        if char == '1':
            epsilon += '0'
        else:
            epsilon += '1'
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == '__main__':
    binaries = load_text_file('input.txt', __file__, lambda s: s)
    print(calculate_rates(binaries))
