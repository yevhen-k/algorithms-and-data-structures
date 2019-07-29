def count_sort(lst: list) -> list:
    """
    count sort for list of integer numbers
    """
    freq = {}
    minval, maxval = lst[0], lst[0]
    for i in lst:
        freq[i] = freq.get(i, 0) + 1
        if i < minval:
            minval = i
        if i > maxval:
            maxval = i
    result = []
    for i in range(minval, maxval + 1):
        if freq.get(i) > 0:
            result += [i] * freq.get(i)
    return result
