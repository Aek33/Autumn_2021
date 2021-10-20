import random
from service import if_str


def quickSort(list_):
    """
    Quick sort function

    Quicksort algorithm works by selecting a 'pivot' element from the array and partitioning the other
    elements into two sub-arrays, according to whether they are less than or greater than the pivot.
    """
    list_ = if_str(list_)
    if len(list_) <= 1:
        return list_
    else:
        pivot = random.choice(list_)
    left_nums = [n for n in list_ if n < pivot]
    middle_nums = [pivot] * list_.count(pivot)
    right_nums = [n for n in list_ if n > pivot]
    return quickSort(left_nums) + middle_nums + quickSort(right_nums)
