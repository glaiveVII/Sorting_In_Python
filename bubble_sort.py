#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:43:21 2019

@author: julienpelegri
"""

# algorithme bubble sort :
 
def bubble_sort(array):
    # array the list we want to sort 
	Bool=True
	while Bool:
		Bool=False
        
		for i in range(1,len(array)):
			if array[i-1]>array[i]:
				array[i],array[i-1] = array[i-1],array[i]
				Bool=True
	return l


# a little test to check 

l = [4,3,2,1,10,0,8,3]
print("the list we want to sort: ",l)

l = bubble_sort(l)
print("the list l sorted : ",l)