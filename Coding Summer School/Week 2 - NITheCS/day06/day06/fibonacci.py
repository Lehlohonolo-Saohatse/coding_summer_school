# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 10:26:59 2025

@author: Lehlo
"""
def fibonacci(n):
    if n < 2:
        return n
    f_minus_two, f_minus_one = 0, 1
    for _ in range(2, n+1):
        current = f_minus_one + f_minus_two
        f_minus_two, f_minus_one = f_minus_one, current
    return f_minus_one
def main():
    #Demonstration of the first 5 fibonacci numbers
    for i in range(6):
        print(f"F({i}) = {fibonacci(i)}")
if _name_ == "_main_":
    main()
