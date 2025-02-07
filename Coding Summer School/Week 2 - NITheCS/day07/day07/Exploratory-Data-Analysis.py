# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os
os.chdir(r"C:\Users\Lehlo\OneDrive - North-West University\Desktop\Coding Summer School\Week 2 - NITheCS\day07\day07")

#%%
# Import the data
animals = pd.read_csv('super-animals.csv')

#%%
# Obtain the variable names included in the data set
list(animals)

# Obtain the number of observations
animals.shape[0]

# Obtain the number of columns
animals.shape[1]

# Draw a histogram for the size of the animals
size = sns.histplot(data = animals, x = "Size",
                    color = "lightblue",
                    edgecolor = "blue",
                    bins = 10)
size.set(ylabel = "Frequency",
         title = "Histogram of the size (in cm) of the animals")
plt.show()

#%%
# Which animal species are included in the data set?
# Make a frequency table
species = animals["Species"].value_counts()

# Calculate the proportions in the frequency table
species_proportions = animals["Species"].value_counts(normalize = True)

# Draw a barplot of the animal species included in the data set.
spec = sns.barplot(x=species.index, y=species.values)
spec.set(ylabel = "Frequency",
         title = "Barplot of the species of animals")
plt.show()

#%%
# Create a two-way frequency table of the categories and the species
twoway = pd.crosstab(animals["Category"], animals["Species"])

#%%
# Recode the vulnerability column
# 1 - Critically endangered (CR)
# 2 - Vulnerable (VU)
# 3 - Near Threatened (NT)
# 4 - Least Concern (LC)
recode_dict = {1: "CR",
               2: "VU",
               3: "NT",
               4: "LC"}

animals["Vulnerability"] = animals["Vulnerability"].map(recode_dict)

#%%
# Create a data set that only contains the birds (subset)
birds = animals.loc[animals["Species"] == "Bird", :]

# Create a frequency table of the vulnerability indices of the birds.
birds_vulnerability = birds["Vulnerability"].value_counts()

# Draw a barplot of the vulnerability indices of the birds.
sns.barplot(x=birds_vulnerability.index, y=birds_vulnerability.values)

# Sort the vulnerability index
birds_vulner_sorted = birds_vulnerability.reindex(["CR", "VU", "NT", "LC"])

sns.barplot(x=birds_vulner_sorted.index, y=birds_vulner_sorted.values)
plt.show()

#%%
# Obtain a quick summary of the size of the birds
summary = birds["Size"].describe()

# Average size of the birds
birds["Size"].mean()
print("Mean: ",summary["mean"])

# Minimum size of the birds
birds["Size"].min()
print("Minimum:", summary["min"])

# Maximum size of the birds
birds["Size"].max()
print("Maximum:", summary["max"])

# Standard deviation of the size of the birds
birds["Size"].std()
print("Standard deviation: ", summary["std"])

#%%
# Draw a histogram for the size of the birds
sns.histplot(data = birds, x = "Size")

# Draw a boxplot for the size of the birds
sns.boxplot(data = birds, x = "Size")
plt.show()

#%%
# Median of the size of the birds
birds["Size"].median()
print("Median: ", summary["50%"])

# Interquartile range of the size of the birds
print("Interquartile range: ", summary["75%"] - summary["25%"])

#%%
# Draw a scatterplot of the size vs the weight of the birds
sns.scatterplot(data = birds, x = "Size", y = "Weight")
plt.show()

#%%
# Do a log transformation on the size and the weight of the birds
birds_log_size = np.log(birds["Size"])
birds_log_weight = np.log(birds["Weight"])

# Draw a scatterplot
sns.scatterplot(x = birds_log_size, y = birds_log_weight)
plt.show()

#%%
## EXPLORING NUMERICAL DATA ACROSS CATEGORIES

# Create a five number summary for the size variable per species
sum_species = animals.groupby(["Species"])["Size"].describe()

# You can use any of the summary statistics function too 
animals.groupby(["Species"])["Size"].mean()
animals.groupby(["Species"])["Size"].median()
animals.groupby(["Species"])["Size"].std()

#%%
# Subset the birds and the mammals
birds_mammals = animals.loc[animals["Species"].isin(["Bird","Mammal"]), :]

# Draw a side-by-side boxplot
sns.boxplot(data = birds_mammals, x = "Size", y = "Species")
plt.show()



