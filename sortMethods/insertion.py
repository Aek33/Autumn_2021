import sortMethods


def insertionSort(_list_):
    """
    Insertion sort function

    Insertion sort algorithm virtually split array into a sorted and an unsorted part.
    Values from the unsorted part are picked and placed at the correct position in the sorted part.
    :param _list_: list with numeric or string values
    :return: sorted list
    """
    _list_ = sortMethods.if_str(_list_)
    if len(_list_) <= 1:
        return _list_
    else:
        for i in range(1, len(_list_)):
            value = _list_[i]
            prev = i - 1
            while prev >= 0 and value < _list_[prev]:
                _list_[prev + 1] = _list_[prev]
                prev -= 1
            _list_[prev + 1] = value
        return _list_

