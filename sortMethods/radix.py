import sortMethods


def radixSort(_list_):
    """
    Radix sort function

    For a list of numbers only!
    Radix Sort is sorting by numbers, from least significant to most significant.
    Radix sort uses counting sort as a sorting routine.
    :param _list_: list with numeric values
    :return: _list_: sorted list
    """
    _list_ = sortMethods.if_str(_list_, True)
    if len(_list_) <= 1:
        return _list_
    else:
        maxEl = max(_list_)

        degree = 1
        while maxEl > 0:
            maxEl /= 10
            degree += 1

        _value_ = 1

        def countingSort(_list_, value):
            """
            Radix sort inner function

            For a list of numbers only!
            Counting Sort works by counting the number of elements,
            that fit a distinct key grid, and then calculates the positions of each key.

            :param _list_: input list for sorting
            :param value: the degree of the numbers to be sorted

            :return outputList: sorted list
            """
            countList = [0] * 10
            listLen = len(_list_)

            for i in range(listLen):
                element = (_list_[i] // value) % 10
                countList[element] += 1

            for i in range(1, 10):
                countList[i] += countList[i - 1]

            outputList = [0] * listLen
            i = listLen - 1
            while i >= 0:
                currEl = _list_[i]
                element = (_list_[i] // value) % 10
                countList[element] -= 1
                newPosition = countList[element]
                outputList[newPosition] = currEl
                i -= 1

            return outputList

        while degree > 0:
            _list_ = countingSort(_list_, _value_)
            _value_ *= 10
            degree -= 1

        return _list_
