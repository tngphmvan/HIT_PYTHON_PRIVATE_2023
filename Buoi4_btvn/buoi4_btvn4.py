# -*- coding: utf-8 -*-
"""buoi4_btvn4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mZJ9IroDbWIZ1wr4NMD5rfMSv6T13KiJ
"""

def check_even_odd(array):
    sum_even = 0
    sum_odd = 0
    for number in array:
        if number % 2 == 0:
            sum_even += number
        else:
            sum_odd += number

    if sum_even > sum_odd:
        return "even"
    elif sum_even < sum_odd:
        return "odd"
    else:
        return "equal"

array = list(map(int, input().split(" ")))
print(check_even_odd(array))