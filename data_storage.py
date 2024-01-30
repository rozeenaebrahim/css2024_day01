# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:08 2024

@author: rebrahim
"""

"""
storing data in Python
1. Lists
2. Dictionaries
3. Data frames
"""

import pandas as pd

file = pd.read_csv("country_data.csv")

print(file)

"""
   Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

age = [39,25,29,46]
print(age[0])

gender = ["M","F","F"]

print(age[0:2])

age.append(100)

mammals={"cat":"a cute animal", "lion":"king of the jungle","elephant":"a gigantic herbivore"}
print(mammals["cat"])

"""
Data frames 
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
Size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
    'fruits': fruits,
    'sizes': Size_nm
    }



df = pd.DataFrame(fruit_sizes) #dataframe
print(df['fruits'])
print(df['sizes'])
print(df['sizes'].min())
print(df['sizes'].max())
print(df['sizes'].describe())
print(df[df["sizes"]> 10])
print(df[1:3])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices']=prices #add column to df

df.drop(columns=["sizes"],inplace=True) #inplace=True