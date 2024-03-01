#!/usr/bin/python3
""" Find the peak module """


def find_peak(list_of_integers):
    """ Return the peak of a list of unsorted integers """
    arr = list_of_integers
    size = len(arr)
    start, end = 0, size - 1

    if arr == []:
        return None
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return arr[mid]
        if arr[mid - 1] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return arr[start]
