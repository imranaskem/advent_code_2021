from utils.utils import load_text_file


def calculate_distance(instructions: list) -> int:
    forward_move = sum([int(move) for ins, move in instructions if ins == 'forward'])
    net_depth = sum([int(move) for ins, move in instructions if ins == 'down']) \
        - sum([int(move) for ins, move in instructions if ins == 'up'])
    return forward_move * net_depth


if __name__ == '__main__':
    instructions = load_text_file('input.txt', __file__, lambda s: s.split(' '))
    print(calculate_distance(instructions))
