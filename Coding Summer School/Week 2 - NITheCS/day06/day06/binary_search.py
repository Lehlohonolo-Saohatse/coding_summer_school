# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 13:40:47 2025

@author: Lehlohonolo Saohatse
"""

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    
    while left <= right:
        mid = (left + right)//2
        
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
            
        elif arr[mid] > target:
            right = mid - 1
            
    return -1

if __name__ == "__main__":
    arr = [1,3,7,9,15,43,101,135]
    target = 101
    
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Elements not found in the array")
