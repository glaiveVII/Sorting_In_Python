#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:47:46 2019

@author: julienpelegri
"""
from random import randint
import time



# selection sort algorithm in python  

def create_array(length=20,maxi=50):
	from random import randint
	return [randint(-maxi,maxi) for _ in range(length)]



def selection_sort(array):
	sort_idx = 0 # end of sorted portion of array
	while sort_idx<len(array):
		min_idx=array[sort_idx:].index(min(array[sort_idx:]))+sort_idx
		array[sort_idx],array[min_idx]=array[min_idx],array[sort_idx]
		sort_idx+=1
	return array 




# wew check our programm
l = create_array()
print("The list we want to sort: ", l)
t0 = time.time()         
l = selection_sort(l)
tot = 0
tot += (time.time() - t0)
print("The list l sorted: ", l)
print('It takes', tot, 'secondes, to sort the array.')