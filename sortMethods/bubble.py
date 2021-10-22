import sortMethods


def bubbleSort(_list_):
    """
    Bubble sort function

    Bubble Sort is the simplest sorting algorithm that works by repeatedly
    swapping the adjacent elements if they are in wrong order.
    :param _list_: list with numeric or string values
    :return: _list_: sorted list
    """
    _list_ = sortMethods.if_str(_list_)
    if len(_list_) <= 1:
        return _list_
    else:
        for i in range(len(_list_)):
            for j in range(0, len(_list_) - 1):
                if _list_[j] > _list_[j + 1]:
                    _list_[j], _list_[j + 1] = _list_[j + 1], _list_[j]
        return _list_

