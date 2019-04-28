#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:05:18 2019

@author: julienpelegri
"""
from random import randint
import time

#  Implementation of MergeSort in Python 3.7

def create_array(length=5,maxi=50):
	return [randint(0,maxi) for _ in range(length)]


def merge_Sort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        merge_Sort(L) # Sorting the first half 
        merge_Sort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
  
# Code to print the list 
def printList(arr): 
    for i in range(len(arr)):         
        print(arr[i],end=" ") 
    print() 
    
    
  
# wew check our programm
l = create_array()

print ("Given array is", end="\n")  
printList(l) 
t0 = time.time()   
merge_Sort(l)
tot += (time.time() - t0) 
print("Sorted array is: ", end="\n") 
printList(l) 
print('It takes', tot, 'secondes, to sort the array.')


  
# This code is contributed by Julien PELEGRI