#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 21 10:25:10 2025

@author: evasorge
"""

#Part 4:
#1)

import seaborn as sns
import pandas as pd
data = pd.read_csv('wdi_wide.csv')

GNI = data["GNI"]
life_expectancy_male = data["Life expectancy, male"]
life_expectancy_female = data["Life expectancy, female"]

    
graph_1 = sns.relplot(x=GNI, y=life_expectancy_male)
print(graph_1)