from day_04.day_04 import calculate_score, process_file
from utils.utils import load_text_file_process


def test_calculate_score():
    numbers, boards = load_text_file_process('day04_input.txt', __file__, process_file)
    assert calculate_score(numbers, boards) == 4512
