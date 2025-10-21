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
import seaborn as sns
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





