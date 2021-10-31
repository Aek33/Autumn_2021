import unittest
import Sudoku
from unittest.mock import patch


class TestSudoku(unittest.TestCase):
    def setUp(self):
        not_solved = "000950760007013800400000090000300100039000080840069000095621078600000015174890023"
        solved = "538471296219865473467329518986537124175642839324918657852796341741283965693154782"
        self.sudoku_f = Sudoku.Sudoku(not_solved)
        self.sudoku_t = Sudoku.Sudoku(solved)

    def test_Sudoku_init(self):
        """Checking the class initializer for correct operation, as well as catching errors"""
        self.assertEqual(self.sudoku_f.check_set, {"1", "2", "3", "4", "5", "6", "7", "8", "9"})
        i_test = {3, 4, 6, 7, 11, 13, 14, 15, 18, 25, 30, 33, 37, 38, 43, 45, 46, 49,
                  50, 55, 56, 57, 58, 59, 61, 62, 63, 70, 71, 72, 73, 74, 75, 76, 79, 80}
        self.assertSetEqual(self.sudoku_f.immutable_val, i_test)
        with self.assertRaises(ValueError):
            Sudoku.Sudoku("002156456")
        with self.assertRaises(TypeError):
            Sudoku.Sudoku(0)
        with self.assertRaises(TypeError):
            str_ = "aaa950760007013800400000090000300100039000080840069000095621078600000015174890023"
            Sudoku.Sudoku(str_)
        with self.assertRaises(TypeError):
            str_ = "0.0950760007013800400000090000300100039000080840069000095621078600000015174890023"
            Sudoku.Sudoku(str_)

    @patch('builtins.input', side_effect=["1", "1", "1"])
    def test_input_value(self, mock_inputs):
        """Checking input_value() for correct operation"""
        self.sudoku_f.input_value()
        self.assertEqual("".join(self.sudoku_f.grid),
                         "100950760007013800400000090000300100039000080840069000095621078600000015174890023")

    def test_check_rows(self):
        """
        Rows check contains 3 tests: when the puzzle is solved, when only the rows converge,
        when nothing converges or there are no values
        """
        only_rows = "123456789123456789123456789123456789123456789123456789123456789123456789123456789"
        self.sudoku_r = Sudoku.Sudoku(only_rows)
        # Puzzle solved
        self.assertTrue(self.sudoku_t.check_rows())
        # Solved only rows
        self.assertTrue(self.sudoku_r.check_rows())
        # Not solved one or all rows
        self.assertFalse(self.sudoku_f.check_rows())

    def test_check_columns(self):
        """
        Columns check contains 3 tests: when the puzzle is solved, when only the columns converge,
        when nothing converges or there are no values
        """
        only_columns = "111111111222222222333333333444444444555555555666666666777777777888888888999999999"
        self.sudoku_c = Sudoku.Sudoku(only_columns)
        # Puzzle solved
        self.assertTrue(self.sudoku_t.check_columns())
        # Solved only columns
        self.assertTrue(self.sudoku_c.check_columns())
        # Not solved one or all columns
        self.assertFalse(self.sudoku_f.check_columns())

    def test_check_boxes(self):
        """
        Boxes check contains 3 tests: when the puzzle is solved, when only the boxes converge,
        when nothing converges or there are no values
        """
        only_boxes = "123123123456456456789789789123123123456456456789789789123123123456456456789789789"
        self.sudoku_b = Sudoku.Sudoku(only_boxes)
        # Puzzle solved
        self.assertTrue(self.sudoku_t.check_boxes())
        # Solved only boxes
        self.assertTrue(self.sudoku_b.check_boxes())
        # Not solved one or all boxes
        self.assertFalse(self.sudoku_f.check_boxes())

    @patch('builtins.input', side_effect=["1", "1", "5"])
    def test_game(self, mock_inputs):
        """The test simulates a game in which there is only one move left to win"""
        grid = "038471296219865473467329518986537124175642839324918657852796341741283965693154782"
        self.sudoku_game = Sudoku.Sudoku(grid)
        self.sudoku_game.input_value()
        self.assertEqual(self.sudoku_game.game(), f"You made {self.sudoku_game.count} turns")


if __name__ == '__main__':
    unittest.main()
