# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 05:57:54 2018

@author: owner
"""

#%%

# Bubble sort implementation.
#
# This function returns nothing because it works by mutating the lst.
def bubble(lst):
    for j in range(0, len(lst) - 1):
        for i in range(0, len(lst) - j - 1):
            if lst[i] > lst[i + 1]:
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                
#%%
                
def merge(left, right):
    result = []

    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
            
    if len(left) == 0:
        result += right
    else:
        result += left
            
    return result  

#%%
    