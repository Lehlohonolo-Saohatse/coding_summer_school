# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 14:27:41 2025

@author: Lehlo
"""

def binary_search_with_duplicates(arr, target):
    left, right = 0, len(arr) - 1
    first_occurrence = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            first_occurrence = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first_occurrence


if __name__ == "__main__":
    arr = [1, 3, 5, 5, 5, 7, 29, 101]
    target = 5
    result = binary_search_with_duplicates(arr, target)
    if result != -1:
        print(f"Elemen {target} found at index {result} (first occurrence)")
    else:
        print(f"Element {target} not found in the array")
    arr = [1, 3, 5, 7, 29, 101]  # Example without duplicates
    target = 5
    result = binary_search_with_duplicates(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result} (first occurrence)")
    else:
        print(f"Element {target} not found in the array")
    arr = [ [1, 3, 5, 7, 29, 101]] # Example without target
    target = 7
    result = binary_search_with_duplicates(arr, target)
    if result != -1:
        print(f"Element {target} found at index {result} (first occurrence)")
    else:
        print(f"Element {target} not found in the array")
