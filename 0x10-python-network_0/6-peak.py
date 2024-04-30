#!/usr/bin/python3
"""Find a peak in a list of unsorted"""
def find_peak(list_of_integers):
    """Find the peak in the list"""
    if list_of_integers is None or list_of_integers == []:
        return None

    lo = 0
    h = len(list_of_integers)
    mid = ((h - lo) // 2) + lo
    mid = int(mid)

    if h == 1:
        return list_of_integers[0]
    if h == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[mid:])
