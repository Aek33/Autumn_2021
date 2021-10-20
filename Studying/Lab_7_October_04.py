# Working with Files

"""
1 Copy contents of one file to another file
2 Create a duplicate file from an existing file.
3 Extract information from an online page to a file.
"""

print("Task 1")


def read_txt(txt_name):
    txt_file = open(txt_name, encoding="utf = 8")
    print(txt_file.read())
    txt_file.close()


def copy_data_to_file(txt_1_name, txt_2_name):
    text_1 = open(txt_1_name, 'r', encoding="utf = 8")
    data = []
    for i in text_1.read():
        data.append(i)
    text_1.close()

    text_2 = open(txt_2_name, 'w', encoding="utf = 8")
    for i in range(len(data)):
        text_2.write(data[i])
    text_2.close()


print("Source file:")
read_txt("test.txt")
print("File to write:")
read_txt("test2.txt")
print("Copying data...")
copy_data_to_file("test.txt", "test2.txt")
print("Copying completed!")

read_txt("test2.txt")

print("Task 2")

import os
import shutil

Direct = r"C:\Users\Baster\Desktop\Новая папка"

print("Before copying file:")
print(os.listdir(Direct))

source = r"C:\Users\Baster\Desktop\PythonProjects\BombyxMori\Studying\test.txt"

copy_to = r"C:\Users\Baster\Desktop\Новая папка\test.txt"

path = shutil.copyfile(source, copy_to)

print("After copying file:")
print(os.listdir(Direct))

print("Path of the duplicate file is:")
print(path)

print("Task 3")

import requests

url = 'https://www.iaea.org/ru'
r = requests.get(url)
with open('test.html', 'w', encoding="utf-8") as output_file:
    output_file.write(r.text)
