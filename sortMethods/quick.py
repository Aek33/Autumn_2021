import random
import sortMethods


def quickSort(_list_):
    """
    Quick sort function

    Quicksort algorithm works by selecting a 'pivot' element from the array and partitioning the other
    elements into two sub-arrays, according to whether they are less than or greater than the pivot.
    :param _list_: list with numeric or string values
    :return: _list_: sorted list
    """
    _list_ = sortMethods.if_str(_list_)
    if len(_list_) <= 1:
        return _list_
    else:
        pivot = random.choice(_list_)
    left_nums = [n for n in _list_ if n < pivot]
    middle_nums = [pivot] * _list_.count(pivot)
    right_nums = [n for n in _list_ if n > pivot]
    return quickSort(left_nums) + middle_nums + quickSort(right_nums)
