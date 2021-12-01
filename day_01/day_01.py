from utils.utils import load_text_file


def calculate_number_depth_increases(depths: list) -> int:
    count = 0
    for i, val in enumerate(depths):
        if i == 0:
            continue
        if val > depths[i-1]:
            count += 1

    return count

if __name__ == '__main__':
    depths = load_text_file('input.txt', __file__)
    print(calculate_number_depth_increases(depths))