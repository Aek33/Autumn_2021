# Lab 8 - Python Decorators
"""
1.Write a decorator program to convert rgb to hex format and vice versa.
2.Write a decorator function that returns dice with the correct amount of eyes in a single string.
3.Write a decorator function to compute the approximative grid of the square root of a number using bisection search.
4.Write a decorator function to create a tic tac toe game to return a win or a draw.
"""

from itertools import combinations_with_replacement
import math


# Task 1
def convert_(fn):
    def wrapper(*args):
        if isinstance(*args, str):
            color_ = str(*args)
            color_ = color_[1:]
            rgb_tuple = tuple(int(color_[i:i + 2], 16) for i in (0, 2, 4))
            return fn(rgb_tuple)
        else:
            color_ = tuple(*args)
            hex_num = "#%02X%02X%02X" % color_
            return fn(hex_num)

    return wrapper


@convert_
def print_color(c):
    print(c)


# Task 2
dice_patterns = {1: "|___|_0_|___|", 2: "|__0|___|0__", 3: "|__0|_0_|0__|",
                 4: "|0_0|___|0_0|", 5: "|0_0|_0_|0_0|", 6: "|0_0|0_0|0_0|"}


def pattern(fn):
    def wrapper():
        new_list = []
        list_of_comb = fn()
        for item in list_of_comb:
            list_of_num = [x for x in item if x != 0]  # if zero in combination list_
            list_of_pattern = [dice_patterns[i] for i in list_of_num]  # replace by pattern
            new_list.append(",".join(list_of_pattern))
        return "\n".join(new_list)

    return wrapper


num = 0


@pattern
def combinations():
    all_comb = list(combinations_with_replacement(range(0, 7), num))  # all possible combinations
    list_of_comb = []
    for tup in all_comb:
        tuple_sum = sum(tup)  # combination must be equal required number
        if tuple_sum == num:
            list_of_comb.append(list(tup))
    return list_of_comb  # now decorator replace numbers by pattern


# Task 3
# https://ru.wikipedia.org/wiki/Метод_бисекции
def approx_val(fn):
    def approximation(value_, acc_):
        left_ = 0
        right_ = value_
        approx_value_ = (left_ + right_) / 2.0
        while abs(approx_value_ ** 2 - value_) >= acc_:
            if (approx_value_ ** 2) < value_:
                left_ = approx_value_
            else:
                right_ = approx_value_
            approx_value_ = (left_ + right_) / 2.0
        value_ = approx_value_
        return fn(value_, acc_)

    return approximation


@approx_val
def approx_1(value_, acc_):
    print(f"Bisection search = {value_} with precision up to {acc_}")


def approx_2(value_):
    print(f"math.sqrt function = {math.sqrt(value_)}")


# Task 4
# initialize columns for playing
board = [[".", ".", "."],
         [".", ".", "."],
         [".", ".", "."]]

# dictionary for input
# reversed values_1 because of pop() function in continue_game()
moves = {"top left": [0, 0], "top": [1, 0], "top right": [2, 0],
         "left": [0, 1], "center": [1, 1], "right": [2, 1],
         "bottom left": [0, 2], "bottom": [1, 2], "bottom right": [2, 2]}


# Decorator. Return winner and end game, or return game() and continue
def chek_winner(func):
    def wrapper(board_f, cond_f, player_f):
        win = False  # counter
        # check columns
        for i in range(len(board_f)):
            for j in range(len(board_f)):
                win = True
                if board_f[i][j] != player_f:
                    win = False
                    break
            if win:
                print(f"Player {player_f} won!")
                return func(board_f, 0, player_f)
        # check columns
        for i in range(len(board_f)):
            for j in range(len(board_f)):
                win = True
                if board_f[j][i] != player_f:
                    win = False
                    break
            if win:
                print(f"Player {player_f} won!")
                return func(board_f, 0, player_f)
        # check diagonals
        win = True
        for i in range(len(board_f)):
            if board[i][i] != player_f:
                win = False
        if win:
            print(f"Player {player_f} won!")
            return func(board_f, 0, player_f)
        # check another diagonal
        win = True
        for i in range(len(board_f)):
            if board[i][len(board_f) - 1 - i] != player_f:
                win = False
        if win:
            print(f"Player {player_f} won!")
            return func(board_f, 0, player_f)
        for i in board_f:
            for j in i:
                if j == ".":
                    return func(board_f, 1, player_f)
        print("Draw!")
        return func(board_f, 0, player_f)

    return wrapper


# This function calling if game is continuing
# Arguments of the game () function are accepted as input,
# as well as input () to change the state of the columns
# Recursion for incorrect grid
# or if the grid has already been entered
def continue_game(board_, player_):
    input_ = input("==>")
    if input_ in moves:
        board[moves[input_].pop()][moves[input_].pop()] = player_
        moves.pop(input_)
        return game(board_, 1, player_)
    elif input_ == "exit":
        return game(board_, 0, player_)
    else:
        print("Incorrect grid, re-enter")
        return continue_game(board_, player_)


def player_switch(player):
    return 'X' if player == 'O' else 'O'


@chek_winner
def game(board_, cond_, player_):
    if cond_ == 0:
        [print(row) for row in board_]
        print("Game over!")
    else:
        [print(row) for row in board_]
        player = player_switch(player_)
        print(f"Now it's {player} turn")
        continue_game(board_, player)


if __name__ == "__main__":
    print("---%s---" % "Task 1")
    print_color((26, 43, 255))
    print_color("#1A2BFF")
    print_color("#000000")
    print_color((1, 1, 1))
    print_color("#FFFFFF")
    print_color((255, 255, 255))

    print("---%s---" % "Task 2")
    num = 7
    print(combinations())

    print("---%s---" % "Task 3")
    approx_1(15, 0.01)
    approx_2(15)
    approx_1(3, 0.001)
    approx_2(3)
    approx_1(4, 0.1)
    approx_2(4)

    print("---%s---" % "Task 4")
    game(board, 1, "O")
