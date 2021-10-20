# Generator Functions for Dictionaries

"""
1. Python – Combine two dictionaries having key of the first dictionary and value of the second dictionary
"""
print("Task 1")
dict_1 = {"One": "eno", "two": "owt", "Three": "eerht"}
dict_2 = {11: 1, 22: 2, 33: 3, 44: 4, 55: 5}
n_dict_1 = {}
count = 0


def dict_keys(d):
    for i in list(d.keys()):
        yield i


def dict_values(d):
    for j in list(d.values_1()):
        yield j


gen_1 = dict_keys(dict_1)
gen_2 = dict_values(dict_2)

while count != len(dict_1):
    n_dict_1.setdefault(next(gen_1), next(gen_2))
    count += 1

print(n_dict_1)

"""
2. Create a Dictionary with Key as First Character and Value as Words Starting with that Character
"""
print("Task 2")
str_1 = input('-->').split()
print()
n_dict_2 = {}
count = 0


def update_dict():
    l = []
    for i in str_1:
        if i[0].upper() not in n_dict_2.keys():
            n_dict_2[i[0].upper()] = []
            n_dict_2[i[0].upper()].append(i)
        elif i not in n_dict_2[i[0].upper()]:
            n_dict_2[i[0].upper()].append(i)
    return n_dict_2


print(update_dict())
"""
3. Extract dictionaries with Empty String value in K key
"""
print("Task 3")
list_3 = [{"One": "eno", "two": "owt", "Three": "eerht", "Key_": ""},
          {"1": "4", "2": "3", "3": "2", "Key_": "1"},
          {"A": "ABCD", "B": "BADC", "C": "ABDC", "Key_": "BACD"}]
K = "Key_"
list_1 = []
K_dict = {}


for dict_ in list_3:
    if dict_[K] == "":
        for i in list_3:
            list_1.append(i[K])

K_dict[K] = list_1
print(K_dict)
