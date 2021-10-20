# Iterators
"""
1 Сreate iterator type that iterates from 10 to a given limit.
2 Create infinite iterator
(A) display multiples of 7 and 9.
(B) To repeat lines 15 number of times.
(C) To repeat a value 38 times.
3 Create an iterator to display
(A) all possible permutations in a given list_.
(B) All possible combinations in list_ with and without replacement in sorted order.
4 Create iterator to swap infinite phrases and singularise plural nouns.
"""

print("Task 1")


# Class
class Task_1:
    def __init__(self, lim):
        self.lim = lim

    def __iter__(self):
        self.n = 10
        return self

    def __next__(self):
        n = self.n
        if n > self.lim:
            raise StopIteration
        else:
            self.n += 1
            return n


for i in Task_1(13):
    print(i)
# or

print("or else")
n = 13
iter_1 = iter(x for x in range(10, n + 1, 1))

while True:
    try:
        print(next(iter_1))
    except StopIteration:
        break

import itertools

print("Task 2 A")

for n in itertools.islice(itertools.count(0), 100):
    if n % 7 == 0 or n % 9 == 0:
        print(n)

print("Task 2 B")

line = ["To repeat lines 15 number of times."]

cycle_1 = itertools.cycle(line)

for i in range(15):
    print(next(cycle_1))

print("Task 2 C")

to_repeat_num = itertools.repeat(83, 38)

while True:
    try:
        print(next(to_repeat_num))
    except StopIteration:
        break

print("Task 3 A")
list_3_A = "all possible permutations in a given list_".split(" ")
gen_3_A = itertools.permutations(list_3_A)

while True:
    try:
        print(next(gen_3_A))
    except StopIteration:
        break

print("Task 3 B")
str_3_B = "All possible combinations in list_".split(" ")
gen_3_B = itertools.combinations(str_3_B, 2)
gen_3_B_rep = itertools.combinations_with_replacement(str_3_B, 5)
list_comb = []
list_comb_rep = []
while True:
    try:
        list_comb.append(next(gen_3_B))
    except StopIteration:
        print(list_comb)
        break

while True:
    try:
        list_comb_rep.append(next(gen_3_B_rep))
    except StopIteration:
        print(list_comb_rep)
        break

print("Task 4")
