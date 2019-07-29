def bubble_sort(lst: list) -> None:
    """
    bubble sort for list of numbres
    """
    n = len(lst)
    for i in range(n):
        for j in range(n - (i + 1)):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def insertion_sort(lst: list) -> None:
    """
    insertion sort for lists of numbers
    """
    n = len(lst)
    for top in range(1, n):
        k = top
        while k > 0:
            if lst[k] < lst[k - 1]:
                lst[k], lst[k - 1] = lst[k - 1], lst[k]
            k -= 1


def choice_sort(lst: list) -> None:
    """
    choice sort for list of numbers
    """
    n = len(lst)
    for i in range(0, n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
