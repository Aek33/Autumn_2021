from heapq import heappush, heappop
import sortMethods


def heapSort(_list_):
    """
    Heap sort function.

    Use library heapq.
    """
    _list_ = sortMethods.if_str(_list_)
    if len(_list_) <= 1:
        return _list_
    else:
        heap = []
        for i in _list_:
            heappush(heap, i)
        _list_ = []
        while heap:
            _list_.append(heappop(heap))
        return _list_
