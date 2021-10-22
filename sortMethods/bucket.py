import sortMethods


# This code is contributed by
# Vinita Yadav

def bucketSort(_list_):
    """
    Bucket sort function

    For a list of numbers only!
    Bucket sort algorithm works by distributing the elements of an array into a number of buckets.
    Each bucket is then sorted individually, either using a different sorting algorithm, or by recursively
    applying the bucket sorting algorithm.
    :param _list_: list with numeric values
    :return: _list_: sorted list
    """
    _list_ = sortMethods.if_str(_list_, True)
    if len(_list_) <= 1:
        return _list_
    else:
        max_e = max(_list_)
        min_e = min(_list_)

        bucket_range = (max_e - min_e) / 5

        bucket_arr = []

        for i in range(5):
            bucket_arr.append([])
        for i in range(len(_list_)):
            diff = (_list_[i] - min_e) / bucket_range - int((_list_[i] - min_e) / bucket_range)
            if diff == 0 and _list_[i] != min_e:
                bucket_arr[int((_list_[i] - min_e) / bucket_range) - 1].append(_list_[i])
            else:
                bucket_arr[int((_list_[i] - min_e) / bucket_range)].append(_list_[i])
        for i in range(len(bucket_arr)):
            if len(bucket_arr[i]) != 0:
                bucket_arr[i].sort()
        k = 0
        for arr in bucket_arr:
            if arr:
                for i in arr:
                    _list_[k] = i
                    k = k + 1
        return _list_

