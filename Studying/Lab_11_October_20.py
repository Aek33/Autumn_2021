from sortMethods import quick
from sortMethods import bubble

list_1 = [8, 7, 9, 5, 9, 1, 5, 99, 0, 1, 0.5]
list_2 = [8, 7, 9, "a", "b", "c", "za", "zb", 0, 3, 1]
q_sort_1 = quick.quickSort(list_1)
q_sort_2 = quick.quickSort(list_2)
print(q_sort_1)
print(q_sort_2)
b_sort_1 = bubble.bubbleSort(list_1)
b_sort_2 = bubble.bubbleSort(list_2)
print(b_sort_1)
print(b_sort_2)

