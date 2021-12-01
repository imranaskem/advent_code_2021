from day_01.day_01 import calculate_number_depth_increases


def test_calculate_number_depth_increases():
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert calculate_number_depth_increases(depths) == 5
