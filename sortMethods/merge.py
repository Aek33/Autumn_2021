import sortMethods


def mergeSort(_list_):
    """
    Merge sort function

    For a list of numbers only!
    Divide the unsorted list into n sublists, each containing one element.
    Repeatedly merge sublists to produce new sorted sublists until there is
    only one sublist remaining. This will be the sorted list.
    :param _list_: list with numeric or string values
    :return _list_: sorted list
    """
    _list_ = sortMethods.if_str(_list_, True)
    if len(_list_) <= 1:
        return _list_
    else:
        _list_ = sortMethods.if_str(_list_)
        left = _list_[:len(_list_) // 2]
        right = _list_[len(_list_) // 2:]
        mergeSort(left)
        mergeSort(right)
        left_count = right_count = list_count = 0
        while left_count < len(left) and right_count < len(right):
            if left[left_count] < right[right_count]:
                _list_[list_count] = left[left_count]
                left_count += 1
            else:
                _list_[list_count] = right[right_count]
                right_count += 1
            list_count += 1
        while left_count < len(left):
            _list_[list_count] = left[left_count]
            left_count += 1
            list_count += 1
        while right_count < len(right):
            _list_[list_count] = right[right_count]
            right_count += 1
            list_count += 1
        return _list_
