def bubble_sort(L: list) -> list:
    """
    bubble sort for list of numbres
    """
    copy = list(L)
    n = len(copy)
    for i in range(n):
        for j in range(n - (i + 1)):
            if copy[j] > copy [j + 1]:
                copy[j], copy [j + 1] = copy[j + 1], copy[j]
    return copy


def insertion_sort(L: list) -> list:
    """
    insertion sort for lists of numbers
    """
    copy = list(L)
    n = len(copy)
    for top in range(1, n):
        k = top
        while k > 0:
            if copy[k] < copy[k - 1]:
                copy[k], copy[k - 1] = copy[k - 1], copy[k]
            k -= 1
    return copy


def choise_sort(L: list) -> list:
    """
    choise sort for list of numbers
    """
    copy = list(L)
    n = len(copy)
    for i in range(0, n):
        for j in range(i + 1, n):
            if copy[i] > copy[j]:
                copy[i], copy[j] = copy[j], copy[i]
    return copy
