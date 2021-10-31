# Unit Testing
"""
Lab 12: Unit Testing
task 1
Write a program to
Return a string representation of an integer
Repeat a substring pattern
Return the longest alternating substring
And finally create a function to perform unit testing on each part of program execution
Task 2
Create a class to pass a string as an argument to Sudoku. Create another class to unit test the performance of sudoku_f.
Matrix 9*9
"""
import unittest


def num_to_word(num):
    I = {0: "", 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
         6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
    X = {0: "Zero", 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
         6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
         11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
         14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
         17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
    XX = {2: 'Twenty', 3: 'Thirty', 4: 'Forty',
          5: 'Fifty', 6: 'Sixty', 7: 'Seventy',
          8: 'Eighty', 9: 'Ninety'}
    if num < 10:
        if num % 10 == 0:
            return f"{X[0]}"
        else:
            return I[num]
    elif num < 100:
        if num < 20:
            return X[num]
        else:
            return f"{XX[num // 10]} {I[num % 10]}"


def repeat(string, nun_of_repeat):
    return string * int(nun_of_repeat)


def longest_sub(sequence):
    current = longest = sequence[0]
    for i in sequence[1:]:
        if int(i) % 2 != int(current[-1]) % 2:
            current += i
        else:
            longest = longest if len(longest) >= len(current) else current
            current = i
    longest = longest if len(longest) >= len(current) else current
    return longest


class TestLabWork(unittest.TestCase):

    def test_num_to_word(self):
        self.assertEqual(num_to_word(99), 'Ninety Nine')

    def test_repeat(self):
        self.assertEqual( repeat("(=`ω´=)", 5), '(=`ω´=)(=`ω´=)(=`ω´=)(=`ω´=)(=`ω´=)')

    def test_longest_sub(self):
        self.assertEqual(longest_sub("894654984654984"), '65498')


