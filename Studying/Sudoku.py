import unittest


# 000950760007013800400000090000300100039000080840069000095621078600000015174890023

class gridCheck:
    """
    Descriptor for sudoku board.
    Checks the game grid and returns the appropriate trigger
    0 - descriptor error
    1 - continue
    2 - puzzle solved

    :return: self.trigger
    """

    def __init__(self):
        self.box_trigger = True
        self.row_trigger = True
        self.column_trigger = True
        self.trigger = 0
        self.check_set = set(map(str, range(1, 10)))

    def __set__(self, instance, value):
        self.grid = value

    def check_rows(self):
        rows = [[self.grid[step:step + 9]] for step in range(0, 81, 9)]
        for row in rows:
            row_to_check = set([i for i in row[0]])
            if row_to_check != self.check_set:
                self.row_trigger = False
                break

    def check_columns(self):  # Можно реализовать через проверку ряда, транспонировав сетку
        columns = [[self.grid[position:73 + position: 9]] for position in range(9)]
        for column in columns:
            column_to_check = set([i for i in column[0]])
            if column_to_check != self.check_set:
                self.column_trigger = False
                break

    def check_boxes(self):
        boxes = [[[self.grid[i: i + 3] for i in range(j, j + 19, 9)]
                  for j in range(k, k + 7, 3)] for k in range(0, 55, 27)]
        for row in boxes:
            for box in row:
                box_to_check = set("".join(box))
                if box_to_check != self.check_set:
                    self.box_trigger = False
                    break

    def __get__(self, instance, owner):
        self.check_rows()
        self.check_columns()
        self.check_boxes()
        if self.row_trigger and self.column_trigger and self.box_trigger:
            self.trigger = 2
        else:
            self.trigger = 1
        return self.trigger


class Sudoku:
    check = gridCheck()

    def __init__(self, str_):
        self.grid = [str_[i] for i in range(81)]

    def insert(self, place, value):
        """
        Descriptor for input
        """
        if place not in set(range(1, 82)):
            print("Invalid input, select a value from 1 to 81")
            return "error"
        if value not in set(range(1, 10)):
            print("Invalid input, select a value from 1 to 9")
            return "error"
        self.grid[place - 1] = str(value)
        return self.grid

    def new_game(self):
        insert = self.insert(int(input("Input place:")), int(input("Input value:")))
        if insert == "error":
            return self.new_game()
        self.check = "".join(insert)
        trigger = self.check
        if trigger == 1:
            self.new_game()
        elif trigger == 2:
            print("Puzzle solved!")




sudoku = Sudoku("000950760007013800400000090000300100039000080840069000095621078600000015174890023")
sudoku.new_game()
"""
class TestLabWork(unittest.TestCase):
    check = gridCheck()

    def test_chek_r(self):
        self.check = "000950760007013800400000090000300100039000080840069000095621078600000015174890023"
        check = self.check
        self.assertEqual(check, 1)
"""
