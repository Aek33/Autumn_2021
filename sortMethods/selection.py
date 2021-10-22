import sortMethods


def selectionSort(_list_):
    """
    Selection sort function

    For a list of numbers only!
    Selection Sort algorithm sorts an array by finding the minimum value
    of the unsorted part and then swapping it with the first unsorted element.
    :param _list_: list with numeric values
    :return: _list_: sorted list
    """
    _list_ = sortMethods.if_str(_list_, True)
    if len(_list_) <= 1:
        return _list_
    else:
        for i in range(len(_list_)):
            min_index = i
            for j in range(i + 1, len(_list_)):
                if _list_[j] < _list_[min_index]:
                    min_index = j
            _list_[i], _list_[min_index] = _list_[min_index], _list_[i]
        return _list_
