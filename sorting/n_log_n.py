TIMSORT_PARTITION_SIZE = 32


def quicksort(lst: list) -> list:
    """
    quick sort for list of numbers
    """
    copy = list(lst)
    low = 0
    high = len(copy) - 1
    _quicksort(copy, low, high)
    return copy


def _quicksort(lst: list, low: int, high: int) -> None:
    if low < high:
        partition = _partition(lst, low, high)
        _quicksort(lst, low, partition - 1)
        _quicksort(lst, partition + 1, high)


def _partition(lst: list, low: int, high: int) -> int:
    pivot = lst[high]
    min_idx = low - 1
    for j in range(low, high):
        if lst[j] <= pivot:
            min_idx += 1
            lst[min_idx], lst[j] = lst[j], lst[min_idx]
    lst[min_idx + 1], lst[high] = lst[high], lst[min_idx + 1]
    return min_idx + 1


def mergesort(lst: list) -> list:
    """
    merge sort for list of numbers
    """
    if len(lst) > 1:
        mid = int(len(lst) / 2)
        l = mergesort(lst[:mid])
        r = mergesort(lst[mid:])
        res = _merge(l, r)
        return res
    return lst


def _merge(lst1: list, lst2: list) -> list:
    len1 = len(lst1)
    len2 = len(lst2)
    res = [0] * (len1 + len2)
    i, j, k = 0, 0, 0
    while i < len1 and j < len2:
        if lst1[i] <= lst2[j]:
            res[k] = lst1[i]
            k += 1
            i += 1
            continue
        if lst2[j] <= lst1[i]:
            res[k] = lst2[j]
            k += 1
            j += 1
            continue
    # dealing with last element in res
    while i < len1:
        res[k] = lst1[i]
        k += 1
        i += 1
    while j < len2:
        res[k] = lst2[j]
        k += 1
        j += 1
    return res


def timsort(lst: list, partition_size=TIMSORT_PARTITION_SIZE) -> None:
    """
    timsort algorithm for sorting lists of numbers
    """
    for i in range(0, len(lst), partition_size):
        _insertion_sort_partitioned(lst, i, min((i+1) * partition_size, len(lst)-1))
    size = partition_size
    while size < len(lst):
        for start in range(0, len(lst), 2*size):
            end = min(start+2*size-1, len(lst)-1)
            mid = start + size - 1
            _merge_timsort(lst, start, mid, end)
        size *= 2


def _insertion_sort_partitioned(lst: list, start: int, end: int) -> None:
    for top in range(start, end + 1):
        k = top
        while k > start:
            if lst[k] < lst[k - 1]:
                lst[k], lst[k - 1] = lst[k - 1], lst[k]
            k -= 1


def _merge_timsort(lst: list, start: int, mid: int, end: int) -> None:
    l = lst[:mid]
    r = lst[mid:]
    len1 = len(l)
    len2 = len(r)
    
    i = j = 0
    k = start
    while i < len1 and j < len2:
        if l[i] <= r[j]:
            lst[k] = l[i]
            k += 1
            i += 1
            continue
        if r[j] <= l[i]:
            lst[k] = r[j]
            k += 1
            j += 1
            continue
    while i < len1:
        lst[k] = l[i]
        k += 1
        i += 1
    while j < len2:
        lst[k] = r[j]
        k += 1
        j += 1


def heapsort(lst: list) -> None:
    """
    heapsort algorithm for list of numbers
    """
    last_elem_idx = len(lst)
    _heapify(lst, last_elem_idx)
    for i in range(last_elem_idx - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        _heapify(lst, i)


def _heapify(lst: list, root: int) -> None:
    for i in range(root):
        largest = i
        left_leaf = 2*i + 1
        right_leaf = 2*i + 2
        if left_leaf < root and lst[left_leaf] > lst[largest]:
            largest = left_leaf
        if right_leaf < root and lst[right_leaf] > lst[largest]:
            largest = right_leaf
        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            _heapify(lst, largest)
