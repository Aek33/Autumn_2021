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
