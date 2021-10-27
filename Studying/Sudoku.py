import unittest


# 000950760007013800400000090000300100039000080840069000095621078600000015174890023

class gridCheck:
    """
    Descriptor for sudoku board.
    Checks the game grid and returns the appropriate trigger
    0 - descriptor error
    1 - continue
    2 - puzzle solved
    3 - input error

    :return: self.trigger
    """

    def __init__(self):
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

    def __get__(self, instance, owner):
        if len(instance) != 81:
            self.trigger = 3  # Ошибка входной величны, проверьте ввод
        else:
            self.check_rows()
            self.check_columns()
            if self.row_trigger and self.column_trigger:
                self.trigger = 2
            else:
                self.trigger = 1
        return self.trigger


"""
class TestLabWork(unittest.TestCase):
    check = gridCheck()

    def test_chek_r(self):
        self.check = "000950760007013800400000090000300100039000080840069000095621078600000015174890023"
        check = self.check
        self.assertEqual(check, 1)
"""