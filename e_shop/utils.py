import itertools
def price_show(value):
    value = str(value)
    value = list(value)
    value.reverse()
    index = 0
    reversed_list = []
    for item in value:
        if index % 3 == 0 and index != 0:
            reversed_list.append(',')
            reversed_list.append(item)
            index += 1
        else:
            reversed_list.append(item)
            index += 1
    reversed_list.reverse()
    str_num = ''
    for num in reversed_list:
        str_num += num

    return str_num
def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))