#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 11:55:39 2019

@author: julienpelegri
"""
from random import randint
import time

    
# insertion sort algorithm in python   
    
# creates randomized arrays for testing my programm 
def create_array(size=10,max=50):
    # we generate random number in (-max,max)
	return [randint(-max,max) for _ in range(size)]


# executes insertion sort on the input array 
def insertion_sort(array):
	for sort_len in range(1,len(array)):
		cur_item=array[sort_len] # next item to insert
		insert_idx=sort_len # current index of item
		
        # iterate down until we reach appropriate insertion location
		while insert_idx>0 and cur_item<array[insert_idx-1]:
			array[insert_idx]=array[insert_idx-1] # shift elements to make room
			insert_idx+=-1 # decrement the insertion index
		array[insert_idx]=cur_item # insert at correct location
	return array




# wew check our programm
l = create_array()
print("The list we want to sort: ", l)
t0 = time.time()         
a=insertion_sort(l)
tot = 0
tot += (time.time() - t0)
print("The list l sorted: ", l)
print('It takes', tot, 'secondes, to sort the array')