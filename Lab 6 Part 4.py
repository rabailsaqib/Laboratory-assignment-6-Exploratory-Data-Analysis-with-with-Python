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
life_expectancy_avg = (data["Life expectancy, female"]+data["Life expectancy, male"])/2
data["life_expectancy_female"] = life_expectancy_female
data["life_expectancy_avg"] = life_expectancy_avg


graph_1 = sns.relplot(x=GNI, y=life_expectancy_female)
plt.xlim(0,(0.2e13))
plt.ylabel("Female life expectancy")
plt.xlabel("GNI per capita")
graph_2 = sns.relplot(x=GNI, y=life_expectancy_male)
plt.xlim(0,(0.2e13))
plt.ylabel("Male life expectancy")
plt.xlabel("GNI per capita")

#Yes, generally for both female and male life expectancies, the higher the GNI, the higher the life expectancy. Females however have a higher life expectancy than males, regardless of GNI

#2)
region = data["Region"]
graph_2 = sns.relplot(x=GNI, y=life_expectancy_female, hue=region)
plt.ylabel("Female life expectancy")
plt.xlim(0,(0.2e13))
graph_3 = sns.relplot(x=GNI, y=life_expectancy_male, hue=region)
plt.ylabel("Male life expectancy")
plt.xlim(0,(0.2e13))

#3)

#Rounding data to try to group GNI together to get a variance to calculate sd
rounded_GNI = data["GNI"].round(-11) #grouping GNIs together by losing precision by rounding to the negative

sns.relplot(x=rounded_GNI, y=life_expectancy_avg, hue=region, kind="line", errorbar="sd")
plt.xlim(0,(0.2e13))


#4)
sns.lmplot(data=data, x="GNI", y="life_expectancy_avg", hue="Region")
plt.xlim(0, 2e12) 
plt.ylim(50, 90)
plt.xlabel("GNI per capita")
plt.ylabel("life_expectancy_avg")
plt.title("GNI vs life_expectancy_avg")
plt.show()


#5)

#q1: is there a relationship between teritary education on female and life expectancy
sns.relplot(data=data, x='Tertiary education, female', y='life_expectancy_female', kind="scatter", col="Region")
plt.xlabel("Tertiary Education (Female)")
plt.ylabel("Female Life Expectancy")
plt.show()

#q2  is there a relationship between internet use  on female and life expectancy
sns.relplot(data=data, x='Internet use', y='life_expectancy_female',  kind="scatter", col="Region")
plt.xlabel("Internet Use")
plt.ylabel("Female Life Expectancy")
plt.show()

#q3 is there a relationship between international tourism and internet use 
sns.relplot(data=data, x='International tourism', y='Internet use', kind="scatter" , hue="Region")
plt.xlabel("International Tourism")
plt.ylabel("Internet Use")
plt.show()

#q4 is there a relationship between population and region
sns.relplot(data=data, x='Region', y='Population', kind="scatter", hue="Region")
plt.xlabel("Region")
plt.ylabel("Population")
plt.show()


#q5 is there a relationship between internet use and region
sns.relplot(data=data, x='Region', y='Internet use', kind="scatter" , hue ="Region")
plt.xlabel("Region")
plt.ylabel("Internet Use")
plt.show()

#6)

#a)Is there any association between Internet use and emissions per capita? ( it seems like there is)
sns.relplot(data=data, x='Internet use', y='Greenhouse gas emissions',kind='scatter' , hue='Region', )
plt.xlabel("Internet Use") 
plt.ylabel("Greenhouse gas emissions")
plt.show()

#Yes, there seems to be a positive connection. The scatter plot shows that countries with higher internet use also tend to have higher greenhouse gas emissions per person

#b)Which are the countries with high emissions? (> 0.03)
high_emissions = data[data['Greenhouse gas emissions'] > 0.03]
print(high_emissions['Country Name'])
                     
#c)Is there much variation by region (with respect to high emissions vs Internet use)?
# for this we can put them in col instead of hues and compare such as 
sns.relplot(data=data, x='Internet use', y='Greenhouse gas emissions',kind='scatter' , col='Region', )
plt.xlabel("Internet Use") 
plt.ylabel("Greenhouse gas emissions")
plt.show()
# here we can see that asia has two points that are higher and even america but there isnt really a direct correlation between internet use and high emission

#d)Do all high income economies have high emissions?
high_income_regions = pd.crosstab(data["Region"], data["High Income Economy"])
print(high_income_regions)
#where 0 is "No" and 1 is "Yes"

#no the hight income economies only include america , asia , Europe and Oceania and they all do have high emissions but asia ,america and europe have more as you can see in the previous scatter graph.






