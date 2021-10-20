# Generator functions
# Instead of the return function we use yield
"""
1. Write a program to solve division by 0 using the with statement,
the enter and exit method and exception handling with generator function
"""
print("Task 1")

def division(x):
    for i in range(x, -1, -1):
        yield i / i


div = division(3)

while True:
    try:
        print(next(div))
    except ZeroDivisionError:
        print("Can't divide by zero!")
        break
"""
2. Python program to check if the list_ contains three consecutive common numbers in Python
"""
print("Task 2")
l_1 = [1, 7, 3, 3, 3, 4, 5, 6, 9, 9, 9, 8]


def check(l):
    n_l = []
    for i in range(len(l_1) - 2):
        if l[i] == l[i + 1] and l[i + 1] == l[i + 2]:
            n_l.append(l[i])
    yield n_l


print(next(check(l_1)))
"""
3.	Merge Python key values_1 to list_ using generator functions.
"""
print("Task 3")
l_3 = [{"One": 1, "Two": 2, "Three": 10}, {"Three": 34, "Two": 43, "One": 45}, {"Three": -100, "Two": 11, "One": 0}]


def marge(l):
    empty_dict = {}
    for i in l:
        for j, k in i.items():
            empty_dict.setdefault(j, []).append(k)
    yield empty_dict


print(next(marge(l_3)))
"""
4.	Write a function to compute the total number of lines of code 
in all python files in the specified directory recursively.
"""
print("Task 4")
import os


def count_lines_of_code(direct):
    count = 0
    for file in os.listdir(direct):
        if file.endswith(".py"):
            with open(file, "r", encoding="utf = 8") as f:
                line_count = 0
                for line in f.read().split("\n"):
                    if line.strip() != "":
                        line_count += 1
            print(file, "number of lines =", line_count)
            count += line_count
    return "Sum of lines =", count


count_lines_of_code(r"C:\Users\Baster\Desktop\PythonProjects\BombyxMori\Studying")
