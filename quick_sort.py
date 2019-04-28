#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:51:20 2019

@author: julienpelegri
"""
from random import randint
import time


# quick  sort algorithm in python  




def create_array(length=5,maxi=50):
	return [randint(0,maxi) for _ in range(length)]



def quick_sort(array):
    
	if len(array)<=1: return array
	smaller,equal,larger=[],[],[]
    
	piv=array[randint(0,len(array)-1)] # select random pivot
	for pt in array:
		if   pt<piv:  smaller.append(pt)
		elif pt==piv: equal.append(pt)
		else: larger.append(pt)
	return quick_sort(smaller) + quick_sort(equal) + quick_sort(larger)




# wew check our programm
l = create_array()
print("The list we want to sort: ", l)
t0 = time.time()         
l=quick_sort(l)
tot = 0
tot += (time.time() - t0)
print("The list l sorted: ", l)
print('It takes', tot, 'secondes, to sort the array.')