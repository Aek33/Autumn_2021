from tabulate import tabulate as tb


class Sudoku:

    def __init__(self, start_field):
        if not isinstance(start_field, str):
            raise TypeError("String type required!")
        elif len(start_field) != 81:
            raise ValueError("Requires a string of length 81!")
        for char in start_field:
            if not char.isdecimal():
                raise TypeError("String with integer values is required!")
        else:
            self.grid = [start_field[i] for i in range(81)]
        self.check_set = set(map(str, range(1, 10)))
        self.count = 0
        self.immutable_val = {i for i in range(len(self.grid))
                              if self.grid[i] in self.check_set}

    def input_value(self):
        """function for entering a new value by grid coordinates"""
        column = input("Enter column number ->")
        row = input("Enter line number ->")
        value = input("Enter value ->")
        if column not in self.check_set \
                or row not in self.check_set \
                or value not in self.check_set:
            print("Incorrect value, re-enter!")
            self.input_value()
        else:
            place = (int(row) * 9 - 1) - (9 - int(column))
            if place in self.immutable_val:
                print("You cannot change the originally set numbers, try different coordinates!")
                self.input_value()
            else:
                self.grid[place] = value

    def check_rows(self):
        """
        Function for checking the rows of the grid
        :return: True or False
        """
        _str_ = "".join(self.grid)
        rows = [[_str_[step:step + 9]] for step in range(0, 81, 9)]
        for row in rows:
            row_to_check = set([i for i in row[0]])
            if row_to_check != self.check_set:
                return False
        return True

    def check_columns(self):  # Можно реализовать через проверку ряда, транспонировав сетку
        """
        Function for checking the columns of the grid
        :return: True or False
        """
        _str_ = "".join(self.grid)
        columns = [[_str_[position:73 + position: 9]] for position in range(9)]
        for column in columns:
            column_to_check = set([i for i in column[0]])
            if column_to_check != self.check_set:
                return False
        return True

    def check_boxes(self):
        """
        Function for checking the boxes of the grid
        :return: True or False
        """
        _str_ = "".join(self.grid)
        boxes = [[[_str_[i: i + 3] for i in range(j, j + 19, 9)]
                  for j in range(k, k + 7, 3)] for k in range(0, 55, 27)]
        for row in boxes:
            for box in row:
                box_to_check = set("".join(box))
                if box_to_check != self.check_set:
                    return False
        return True

    def game(self):
        """
        The main function, checks the state of the puzzle,
        displays the grid, continues the game if necessary, updates the move counter
        """
        print(tb({i: self.grid[i:73 + i: 9] for i in range(9)}, tablefmt="simple"))
        if self.check_rows() and self.check_columns() and self.check_boxes():
            print("Puzzle solved!")
            return f"You made {self.count} turns"
        else:
            self.count += 1
            self.input_value()
            return self.game()


if __name__ == "__main__":
    sudoku_1 = Sudoku("008471296219865473467329518986537124175642839324918657852796341741283965693154782")
    print(sudoku_1.game())
