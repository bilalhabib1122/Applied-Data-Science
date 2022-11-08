# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 13:31:49 2022

@author: bh22aaj
"""

import pandas as pd
import matplotlib.pyplot as plt

def get_label(in_para):
    '''decide appropriate lable according to input parameter'''
    if in_para == 'LS':
       result = 'London and South East'
    elif in_para == 'LD':   
      result = 'Long distance'
    elif in_para == 'RE':   
      result = 'Regional'
    elif in_para == 'AO':
      result = 'All operators'
    else:
      result = 'Sorry no label'
    return result    

def get_max_fare(in_para):
    '''returns maximum fare in all the time for input sector'''
    result = round(max(input_file_data[in_para]),2)
    return result

input_file_data = pd.read_excel ('Average change of rail fares in Great Britain.xlsx')

plt.figure(dpi = 144)

width = 0.1
x= ["London and South East","Long distance","Regional","All operators"]

plt.bar(x[0], get_max_fare("London and South East"), width , label = get_max_fare(get_label('LS')))
plt.bar(x[1], get_max_fare("Long distance"), width , label = get_max_fare(get_label('LD')))
plt.bar(x[2], get_max_fare("Regional"), width , label = get_max_fare(get_label('RE')))
plt.bar(x[3], get_max_fare("All operators"), width , label = get_max_fare(get_label('AO')))

plt.xlabel("Year")
plt.ylabel("Fare")
plt.legend()
plt.grid(True)

plt.show()