# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:45:44 2020

@author: danya
"""

# function to get unique values 
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
    ind = []
    # traverse for all elements 
    for ii,x in enumerate(list1): 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
            ind.append(ii)
    return unique_list, ind