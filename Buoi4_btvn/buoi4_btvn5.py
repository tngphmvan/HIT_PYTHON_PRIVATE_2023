# -*- coding: utf-8 -*-
"""buoi4_btvn5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mZJ9IroDbWIZ1wr4NMD5rfMSv6T13KiJ
"""

def flatten(array):
    flat_array = []
    for item in array:
        if isinstance(item, list):
            flat_array += flatten(item)
        else:
            flat_array.append(item)
    return flat_array

array = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
print(flatten(array))