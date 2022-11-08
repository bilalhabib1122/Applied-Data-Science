# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:29:49 2022

@author: bh22aaj
"""

import pandas as pd
import matplotlib.pyplot as plt

def create_lable(in_para):
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
    
input_file_data = pd.read_excel ('Average change of rail fares in Great Britain.xlsx')

plt.figure(dpi = 144)

plt.plot(input_file_data["Year"], input_file_data["London and South East"], label = create_lable('LS'))
plt.plot(input_file_data["Year"], input_file_data["Long distance"], label = create_lable('LD'))
plt.plot(input_file_data["Year"], input_file_data["Regional"], label = create_lable('RE'))
plt.plot(input_file_data["Year"], input_file_data["All operators"], label = create_lable('AO'))

plt.xlabel("Year")
plt.ylabel("Fare")
plt.legend()
plt.grid(True)

plt.show()