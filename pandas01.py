# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 09:32:43 2024

@author: rebrahim
"""

import pandas

file=pandas.read_csv("country_data.csv")

file2=pandas.read_csv("diab_data.csv")

file3=pandas.read_csv("housing_data.csv")

file4=pandas.read_csv("insurance_data.csv",skiprows=5)

#file5=pandas.read_csv("iris.csv")

print(file.info()) #check data is validated - non null values, strings/integers etc.

"""
 <class 'pandas.core.frame.DataFrame'>
 RangeIndex: 11 entries, 0 to 10
 Data columns (total 3 columns):
  #   Column   Non-Null Count  Dtype 
 ---  ------   --------------  ----- 
  0   Age      11 non-null     int64 - WHOLE NUMBER
  1   Gender   11 non-null     object - STRING
  2   Country  11 non-null     object - STRING
 dtypes: int64(1), object(2)
 memory usage: 396.0+ bytes
 None
 
 object=string
"""
print(file4.info())

print(file4.describe()) #stats for numerical data

column_names = ["A","B","C","D","E","F","G","H","I"]
file3=pandas.read_csv("housing_data.csv", names=column_names)
print(file3)




