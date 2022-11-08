# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:29:49 2022

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

def show_graph():
    '''show the plot'''
    plt.show()
    
input_file_data = pd.read_excel ('Average change of rail fares in Great Britain.xlsx')

plt.figure(dpi = 144)

plt.plot(input_file_data["Year"], input_file_data["London and South East"], label = get_label('LS'))
plt.plot(input_file_data["Year"], input_file_data["Long distance"], label = get_label('LD'))
plt.plot(input_file_data["Year"], input_file_data["Regional"], label = get_label('RE'))
plt.plot(input_file_data["Year"], input_file_data["All operators"], label = get_label('AO'))

plt.xlabel("Year")
plt.ylabel("Fare")
plt.legend()
plt.grid(True)

show_graph