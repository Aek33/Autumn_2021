def if_str(list_):
    trigger = False
    for value in list_:
        if isinstance(value, str):
            trigger = True
            break
    if trigger:
        list_ = list(map(str, list_))
        return list_
    else:
        return list_


def bubbleSort(list_):
    """
    Bubble sort function

    Bubble Sort is the simplest sorting algorithm that works by repeatedly
    swapping the adjacent elements if they are in wrong order.
    """
    list_ = if_str(list_)
    if len(list_) < 1:
        return list_
    else:
        for i in range(len(list_)):
            for j in range(0, len(list_) - 1):
                if list_[j] > list_[j + 1]:
                    list_[j], list_[j + 1] = list_[j + 1], list_[j]
        return list_

