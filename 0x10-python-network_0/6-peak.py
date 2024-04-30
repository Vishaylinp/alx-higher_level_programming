#!/usr/bin/python3

def find_peak(list_of_integers):
    """Find the peak in the list"""
    if not list_of_integers:
        return None

    lo = 0
    h = len(list_of_integers) - 1

    while lo < h:
        mid = (lo + h) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            lo = mid + 1
        elif mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            h = mid - 1
        else:
            return list_of_integers[mid]
    return list_of_integers[lo]
