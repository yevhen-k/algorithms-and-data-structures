TIMSORT_PARTITION_SIZE = 32

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


def timsort(L: list, partition_size=TIMSORT_PARTITION_SIZE) -> None:
    """
    timsort algorithm for sorting lists of numbers
    """
    for i in range(0, len(L), partition_size):
        _insertion_sort_partitioned(L, i, min((i+1) * partition_size, len(L)-1))
        # insertion_sort(L[i:min((i+1) * partition_size, len(L)-1)])
    size = partition_size
    while size < len(L):
        for start in range(0, len(L), 2*size):
            end = min(start+2*size-1, len(L)-1)
            mid = start + size - 1
            _merge_timsort(L, start, mid, end)
        size *= 2


def _insertion_sort_partitioned(L: list, start: int, end: int) -> None:
    for top in range(start, end + 1):
        k = top
        while k > start:
            if L[k] < L[k - 1]:
                L[k], L[k - 1] = L[k - 1], L[k]
            k -= 1


def _merge_timsort(L: list, start: int, mid: int, end: int) -> None:
    l = L[:mid]
    r = L[mid:]
    len1 = len(l)
    len2 = len(r)
    
    i = j = 0
    k = start
    while i < len1 and j < len2:
        if l[i] <= r[j]:
            L[k] = l[i]
            k += 1
            i += 1
            continue
        if r[j] <= l[i]:
            L[k] = r[j]
            k += 1
            j += 1
            continue
    while i < len1:
        L[k] = l[i]
        k += 1
        i += 1
    while j < len2:
        L[k] = r[j]
        k += 1
        j += 1


def heapsort(L: list) -> None:
    """
    heapsort algorithm for list of numbers
    """
    last_elem_idx = len(L)
    _heapify(L, last_elem_idx)
    for i in range(last_elem_idx - 1, 0, -1):
        L[0], L[i] = L[i], L[0]
        _heapify(L, i)

def _heapify(L: list, root: int) -> None:
    for i in range(root):
        largest = i
        left_leaf = 2*i + 1
        right_leaf = 2*i + 2
        if left_leaf < root and L[left_leaf] > L[largest]:
            largest = left_leaf
        if right_leaf < root and L[right_leaf] > L[largest]:
            largest = right_leaf
        if largest != i:
            L[i], L[largest] = L[largest], L[i]
            _heapify(L, largest)
