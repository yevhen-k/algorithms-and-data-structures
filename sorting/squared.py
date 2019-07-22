def bubble_sort(L: list) -> None:
    """
    bubble sort for list of numbres
    """
    n = len(L)
    for i in range(n):
        for j in range(n - (i + 1)):
            if L[j] > L [j + 1]:
                L[j], L [j + 1] = L[j + 1], L[j]


def insertion_sort(L: list) -> None:
    """
    insertion sort for lists of numbers
    """
    n = len(L)
    for top in range(1, n):
        k = top
        while k > 0:
            if L[k] < L[k - 1]:
                L[k], L[k - 1] = L[k - 1], L[k]
            k -= 1


def choise_sort(L: list) -> None:
    """
    choise sort for list of numbers
    """
    n = len(L)
    for i in range(0, n):
        for j in range(i + 1, n):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
