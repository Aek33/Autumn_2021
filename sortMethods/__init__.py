# Packages
"""
Create a package, inside the package, create modules to sort characters and values_1.
Sort modules include - quick sort, bubble sort, merge sort, insertion sort, selection sort,
heap sort, radix sort and bucket sort. Finally create a program to execute these sort algorithms
on dynamically entered characters and variables.
"""

__all__ = ["bubble", "bucket", "heap", "insertion",
           "merge", "quick", "radix", "selection"]

from sortMethods import *


def if_str(_list_, only_num=False):
    """
    Function used in all sorting modules

    It is necessary to check input lists for the presence of string variables
    and transform the storage if they are found
    :param only_num: trigger for methods which can't sort string values
    :param _list_: list with numeric or string values
    :return: _list_: modified list
    """
    trigger = False
    for value in _list_:
        if isinstance(value, str):
            trigger = True
            break
    if trigger and not only_num:
        _list_ = list(map(str, _list_))
        return _list_
    elif trigger and only_num:
        raise TypeError("Method for numeric variables only!")
    else:
        return _list_


def quick_sort(list_):
    list_to_return = quick.quickSort(list_)
    return list_to_return


def bubble_sort(list_):
    list_to_return = bubble.bubbleSort(list_)
    return list_to_return


def merge_sort(list_):
    list_to_return = merge.mergeSort(list_)
    return list_to_return


def selection_sort(list_):
    list_to_return = selection.selectionSort(list_)
    return list_to_return


def insertion_sort(list_):
    list_to_return = insertion.insertionSort(list_)
    return list_to_return


def heap_sort(list_):
    list_to_return = heap.heapSort(list_)
    return list_to_return


def radix_sort(list_):
    list_to_return = radix.radixSort(list_)
    return list_to_return


def bucket_sort(list_):
    list_to_return = bucket.bucketSort(list_)
    return list_to_return

