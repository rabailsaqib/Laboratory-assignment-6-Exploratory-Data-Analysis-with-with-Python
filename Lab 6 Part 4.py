#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 10:25:10 2025

@author: evasorge
"""

#Part 4:
#1)
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = pd.read_csv('wdi_wide.csv')

GNI = data["GNI"]
life_expectancy_male = data["Life expectancy, male"]
life_expectancy_female = data["Life expectancy, female"]
life_expectancy_avg = (data["Life expectancy, male"]+data["Life expectancy, female"])/2

graph_1 = sns.relplot(x=GNI, y=life_expectancy_avg)
plt.xlim(0,(0.2e13))
plt.ylabel("Life expectancy average (male and female)")
plt.xlabel("GNI per capita")

#Yes, generally for both female and male life expectancies, the higher the GNI, the higher the life expectancy

#2)
region = data["Region"]
graph_2 = sns.relplot(x=GNI, y=life_expectancy_avg, hue=region)
plt.xlim(0,(0.2e13))

#3)

#Rounding data to try to group GNI together to get a variance to calculate sd
rounded_GNI = data["GNI"].round(-11) #grouping GNIs together by losing precision by rounding to the negative

sns.relplot(x=rounded_GNI, y=life_expectancy_avg, hue=region, kind="line", errorbar="sd")
plt.xlim(0,(0.2e13))


            