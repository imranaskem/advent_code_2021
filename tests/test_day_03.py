from day_03.day_03 import calculate_rates
from utils.utils import load_text_file


def test_calculate_rates():
    binaries = load_text_file('day03_input.txt', __file__, lambda s: s)
    assert calculate_rates(binaries) == 230
