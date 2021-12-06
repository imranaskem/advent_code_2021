from day_02.day_02 import calculate_distance
from utils.utils import load_text_file


def test_calculate_distance():
    instructions = load_text_file('day02_input.txt', __file__, lambda s: s.split(' '))
    assert calculate_distance(instructions) == 900
