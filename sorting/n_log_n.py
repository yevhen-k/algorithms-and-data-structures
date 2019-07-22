def quicksort(L: list) -> list:
    """
    quick sort for list of numbers
    """
    copy = list(L)
    low = 0
    high = len(copy) - 1
    _quicksort(copy, low, high)
    return copy

def _quicksort(L: list, low: int, high: int) -> None:
    if low < high:
        partition = _partition(L, low, high)
        _quicksort(L, low, partition - 1)
        _quicksort(L, partition + 1, high)

def _partition(L: list, low: int, high: int) -> int:
    pivot = L[high]
    min_idx = low - 1
    for j in range(low, high):
        if L[j] <= pivot:
            min_idx += 1
            L[min_idx], L[j] = L[j], L[min_idx]
    L[min_idx + 1], L[high] = L[high], L[min_idx + 1]
    return min_idx + 1


# def mergesort(L: list) -> list:
#     copy = list(L)
#     mid = int((len(copy) - 1) / 2)
#     l = copy[:mid]
#     r = copy[mid:]
#     if len(copy) > 1:
#         _mergesort(l)
#         _mergesort(r)
#     return copy

def mergesort(L: list) -> list:
    """
    merge sort for list of numbers
    """
    if len(L) > 1:
        mid = int( len(L) / 2)
        l = mergesort(L[:mid])
        r = mergesort(L[mid:])
        res = _merge(l, r)
        return res
    return L

def _merge(L1: list, L2: list) -> list:
    len1 = len(L1)
    len2 = len(L2)
    res = [0] * (len1 + len2)
    i, j, k = 0, 0, 0
    while i < len1 and j < len2:
        if L1[i] <= L2[j]:
            res[k] = L1[i]
            k += 1
            i += 1
            continue
        if L2[j] <= L1[i]:
            res[k] = L2[j]
            k += 1
            j += 1
            continue
    # dealing with last element in res
    while i < len1:
        res[k] = L1[i]
        k += 1
        i += 1
    while j < len2:
        res[k] = L2[j]
        k += 1
        j += 1
    return res
