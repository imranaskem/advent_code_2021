from utils.utils import load_text_file_get_num_list


def calculate_number_depth_increases(depths: list) -> int:
    count = 0
    calculated_depths = []
    for i, val in enumerate(depths):
        calculated_depth = val + depths[i+1] + depths[i+2]
        calculated_depths.append(calculated_depth)
        if i == len(depths) - 3:
            break
    for i, val in enumerate(calculated_depths):
        if i == 0:
            continue
        if val > calculated_depths[i-1]:
            count += 1

    return count


if __name__ == '__main__':
    depths = load_text_file_get_num_list('input.txt', __file__)
    print(calculate_number_depth_increases(depths))
