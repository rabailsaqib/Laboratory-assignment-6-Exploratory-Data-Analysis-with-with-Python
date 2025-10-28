#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 08:16:36 2025

@author: evasorge
"""


#Questions to answer:
    #1. Does internet usage affect greenhouse gas emissions?
    #2. How is GNI affected by education?
    #3. What regions are the richest?
    
    

#Load dataset using pandas

import pandas as pd
data = pd.read_csv('wdi_wide.csv')

#Accessing wanted data

GHG = data["Greenhouse gas emissions"]
internet_usage = data["Internet use"]
GNI = data["GNI"]
male_education = data["Tertiary education, male"]
female_education = data["Tertiary education, female"]
regions = data["Region"]

#Question 3:   
data.info()
data.isnull().sum()

#10 null values for Physicians
#0 null values for Population


#Question 4:
data.nunique()
print(data.nunique())


#Question 5:
data.describe()
print(data.describe())

#This function provides the amount of rows and columns our dataset has

#Question 6:
data["GNI per capita"] = (data["GNI"]/data["Population"]).round(2)
print(data["GNI per capita"])

#Question 7:
#a)
nb_of_regions = data["Region"].value_counts()
print(nb_of_regions)

#b)
nb_of_high_income_economies = data["High Income Economy"].value_counts()
print(nb_of_high_income_economies)


#Question 8:
high_income_regions = pd.crosstab(data["Region"], data["High Income Economy"])
print(high_income_regions)
#where 0 is "No" and 1 is "Yes"

#Question 9:
filtered_data = data[data["Life expectancy, female"] > 80]
print(filtered_data)
#66 countries
for i in filtered_data["Country Name"]:
    print(i)
    
    
