# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:42:00 2025

@author: Lehlo
"""
import pandas as pd
import os

os.chdir(r"C:\Users\Lehlo\OneDrive - North-West University\Desktop\Coding Summer School\Week 2 - NITheCS\day07\day07")
truck = pd.read_csv("CoffeeTruck.csv")

#question 1
columns = truck.shape[0]
rows = truck.shape[1]

#Question 2
list(truck)

#Question 3
#Find the unique values in the 'Location' variable. 
#How many unique locations are present in the data set?

values = truck["Location"].unique()

#Question 4
# Subset the data to include only the observations of sales at the Zoo
subset = truck.loc[truck["Location"] == "Zoo", :]

#Question 5
#How many duplicated rows are there in the data? Remove all the duplicated rows from the data set.
#How many rows are left in the data set?

duplicated = truck.duplicated(keep = False)
dups = truck[duplicated]

#Drop duplicates
no_dups = truck.drop_duplicates(keep = "first")

#rows left
no_dups.shape[0]

#Question 6
#Sort the data set first by profit made (from smallest to largest) and then by music played (from Z to A).
#(Make use of the data set where the duplicates are removed.)

sorted_data = no_dups.sort_values(by=['Profit','Music'], ascending=[True,False])

#Question 7
#Create a new variable called ‘Indicator’ that contains the word 'Loss' if the profit for the day is less than
#0, and 'Profit' if the profit for the day is greater than 0. (Make use of the sorted data set.)

def profit_indicator(profit):
    if profit < 0:
        return "Loss"
    else:
        return "Profit"
    
sorted_data["Indicator"] = sorted_data["Profit"].apply(profit_indicator)










