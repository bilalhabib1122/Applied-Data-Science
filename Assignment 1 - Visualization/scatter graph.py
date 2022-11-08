# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 10:40:04 2022

@author: bh22aaj
"""

import pandas as pd
import matplotlib.pyplot as plt

def compare_last_year_fare(in_para):
  for count, value in enumerate(input_file_data['Year']):
    if value == in_para:
      current_year_fare = regional_fares_arr[count]
      if count > 0:
        last_year_fare = regional_fares_arr[count-1]
      else:
        last_year_fare = 0  
      
  if current_year_fare > last_year_fare:
    result = 'green'  
  else:
    result = 'red'
  return result  
    
input_file_data = pd.read_excel ('Average change of rail fares in Great Britain.xlsx')
years_arr = input_file_data['Year']
regional_fares_arr = input_file_data['Regional']
color_array = years_arr.apply(compare_last_year_fare)

plt.figure(dpi = 144)

plt.scatter(input_file_data["Year"], input_file_data["Regional"], label = 'Regional',color = color_array)

plt.xlabel("Year")
plt.ylabel("Fare")
plt.legend()
plt.grid(True)
plt.show()