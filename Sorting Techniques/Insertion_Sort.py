# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r_ESNZfmsamM3vf802CW01GUvfLfgmjs

# Insertion Sort
"""

def insertionsort(a):
    for i in range(len(a) - 1):
        newelement = a[i+1]
        j = i+1
        while j > 0 and a[j-1] > newelement:
            a[j] = a[j-1]
            j-=1
        a[j] = newelement

a = []
size = int(input('Enter size of array: '))
print('')
for i in range(size):
    data = int(input('Enter element: '))
    a.append(data)
print('')
print('Elements are: ',a)

insertionsort(a)
print('After sorting elements are: ',a)