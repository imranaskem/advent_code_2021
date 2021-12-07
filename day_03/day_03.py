import operator

from utils.utils import load_text_file


def calculate_rating(binaries: list, op) -> str:
    binary_length = len(binaries[0]) - 1
    for i in range(0, binary_length):
        if len(binaries) == 1:
            break
        one_list = [bin for bin in binaries if bin[i] == '1']
        zero_list = [bin for bin in binaries if bin[i] == '0']
        if len(one_list) == len(zero_list):
            binaries = one_list.copy() if op == operator.lt else zero_list.copy()
        elif op(len(one_list), len(zero_list)):
            binaries = zero_list.copy()
        else:
            binaries = one_list.copy()
    return binaries[0]


def calculate_rates(binaries: list) -> int:
    co_binary = calculate_rating(binaries.copy(), operator.gt)
    oxygen_binary = calculate_rating(binaries.copy(), operator.lt)
    return int(co_binary, 2) * int(oxygen_binary, 2)


if __name__ == '__main__':
    binaries = load_text_file('input.txt', __file__, lambda s: s)
    print(calculate_rates(binaries))
