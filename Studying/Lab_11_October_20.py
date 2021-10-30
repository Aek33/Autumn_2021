import sortMethods
print("---%s---" % "Original lists")
print([8, 7, 964, 5, 9, 1, 5, 99, 0, 100])
print([8, 7, 9, "c", "b", "a", "zz", "za", 0, 3, 1])
q_sort_1 = sortMethods.quick_sort([8, 7, 964, 5, 9, 1, 5, 99, 0, 100])
q_sort_2 = sortMethods.quick_sort([8, 7, 9, "c", "b", "a", "zz", "za", 0, 3, 1])
print("---%s---" % "Quick sort")
print(q_sort_1)
print(q_sort_2)
b_sort_1 = sortMethods.bubble_sort([8, 7, 964, 5, 9, 1, 5, 99, 0, 100])
b_sort_2 = sortMethods.bubble_sort([8, 7, 9, "c", "b", "a", "zz", "za", 0, 3, 1])
print("---%s---" % "Bubble sort")
print(b_sort_1)
print(b_sort_2)
m_sort_1 = sortMethods.merge_sort([8, 7, 964, 5, 9, 1, 5, 99, 0, 100])
print("---%s---" % "Marge sort")
print(m_sort_1)
i_sort_1 = sortMethods.insertion_sort([8, 7, 964, 5, 9, 1, 5, 99, 0, 100])
i_sort_2 = sortMethods.insertion_sort([8, 7, 9, "c", "b", "a", "zz", "za", 0, 3, 1])
print("---%s---" % "Insertion sort")
print(i_sort_1)
print(i_sort_2)
s_sort_1 = sortMethods.selection_sort([8, 7, 964, 5, 9, 1, 5, 99, 0, 100])
print("---%s---" % "Selection sort")
print(s_sort_1)
h_sort_1 = sortMethods.heap_sort([8, 7, 964, 5, 9, 1, 5, 99, 0, 100])
h_sort_2 = sortMethods.heap_sort([8, 7, 9, "c", "b", "a", "zz", "za", 0, 3, 1])
print("---%s---" % "Heap sort")
print(h_sort_1)
print(h_sort_2)
r_sort_1 = sortMethods.radix_sort([8, 7, 964, 5, 9, 1, 5, 99, 0, 100])
print("---%s---" % "Radix sort")
print(r_sort_1)
bucket_sort_1 = sortMethods.bucket_sort([8, 7, 964, 5, 9, 1, 5, 99, 0, 100])
print("---%s---" % "Bucket sort")
print(bucket_sort_1)