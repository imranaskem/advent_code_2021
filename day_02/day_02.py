from utils.utils import load_text_file


def calculate_distance(instructions: list) -> int:
    aim = 0
    forward_move = 0
    depth = 0
    for ins, move in instructions:
        num_move = int(move)
        if ins == 'forward':
            forward_move += num_move
            depth += aim * num_move
        if ins == 'up':
            aim -= num_move
        if ins == 'down':
            aim += num_move
    return forward_move * depth


if __name__ == '__main__':
    instructions = load_text_file('input.txt', __file__, lambda s: s.split(' '))
    print(calculate_distance(instructions))
