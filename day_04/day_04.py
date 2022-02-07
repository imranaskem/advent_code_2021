from typing import List

from utils.utils import load_text_file_process


class BingoNumber:
    number: int
    marked: bool
    x_position: int
    y_position: int

    def __init__(self, number, x, y) -> None:
        self.number = number
        self.marked = False
        if x > 5 or y > 5:
            raise ValueError('Coordinates can not be more than 5')
        self.x_position = x
        self.y_position = y


class BingoBoard:
    numbers: List[BingoNumber]

    def __init__(self, first_number) -> None:
        self.numbers = [first_number]

    def add_bingo_number(self, bingo_number: BingoNumber):
        self.numbers.append(bingo_number)

    def mark_number(self, number):
        number_to_mark = [num for num in self.numbers if num.number == number]
        if number_to_mark is not None and len(number_to_mark) == 1:
            number_to_mark[0].marked = True

    def check_for_matched_set(self) -> bool:
        matched_numbers = [num for num in self.numbers if num.marked is True]
        if len(matched_numbers) < 5:
            return False
        for i in range(1, 6):
            matched_col = [num for num in matched_numbers if num.x_position == i]
            matched_row = [num for num in matched_numbers if num.y_position == i]
            if len(matched_col) == 5 or len(matched_row) == 5:
                return True
        return False

    def sum_of_non_matched_numbers(self):
        return sum([num.number for num in self.numbers if num.marked is False])


def calculate_score(numbers: List[int], boards: List[BingoBoard]) -> int:
    completed = []
    for num in numbers:
        for board in boards:
            board.mark_number(num)
            if board.check_for_matched_set():
                if board not in completed:
                    completed.append(board)
                if len(completed) == len(boards):
                    final_board = completed[-1]
                    return final_board.sum_of_non_matched_numbers() * num


def process_file(file):
    first_line = True
    board_row = 1
    boards = []
    for line in file:
        if first_line:
            numbers = [int(num) for num in line.rstrip('\n').split(',')]
            first_line = False
        elif line == '\n':
            continue
        else:
            string_list = line.rstrip('\n').split(' ')
            string_list = [val for val in string_list if val != '']
            row = [int(num) for num in string_list]
            x_pos = 1
            for num in row:
                if board_row == 1 and x_pos == 1:
                    board = BingoBoard(BingoNumber(num, x_pos, board_row))
                else:
                    board.add_bingo_number(BingoNumber(num, x_pos, board_row))
                x_pos += 1
            board_row += 1
            if board_row > 5:
                boards.append(board)
                board_row = 1
    return numbers, boards


if __name__ == '__main__':
    numbers, boards = load_text_file_process('input.txt', __file__, process_file)
    print(calculate_score(numbers, boards))
