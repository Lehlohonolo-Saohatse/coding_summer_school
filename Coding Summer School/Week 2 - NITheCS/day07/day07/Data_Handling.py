# CHPC Summer School 2025
# Working with data in Python

# Import packages
import pandas as pd
import os

# Change the file path to where the data is located on your device
os.chdir(r"C:\Users\Lehlo\OneDrive - North-West University\Desktop\Coding Summer School\Week 2 - NITheCS\day07\day07")
#%%
# Import the data
racing = pd.read_csv("RacingGameData.csv")

#%%
# Obtain the variable names included in the data set
list(racing)

# Obtain the number of observations
racing.shape[0]  #rows

# Obtain the number of columns
racing.shape[1]  #columns

# Obtain the data types of each column
racing.dtypes  #data type of each column

#%%
# Display the first 5 observations in the data set
racing.head()

# Display the first 10 observations in the data set
racing.head(10)  #number of rows in the brackets

#%%
# Extract the racing tracks column
tracks = racing["Track"]  #column you're extracting in square bracket

# Show the unique values in the racing tracks column
track_types = racing["Track"].unique() #or tract_types = tracks.unique()

#%%
# Extract row 5 of the data set
racing.iloc[4]  #iloc - index location

# Extract the 5th, 7th and 10th row of the dataset.
extracted = racing.iloc[[4,6,9]]  #row_indexes 5, 6, 9

#%%
# Subset the data set to only contain the races on the "OvalTrack"
racing_oval = racing.loc[racing["Track"] == "OvalTrack", :]

# Subset the data set to only contain the races on either the "StraightTrack" 
# or the "OvalTrack"
tr = ["StraightTrack", "OvalTrack"]
racing_oval_straight = racing.loc[racing["Track"].isin(tr), :]

# Subset the data set to only contain the races on the "OvalTrack" and
# the car that had a "Bayes" engine
racing_oval_bayes = racing.loc[(racing["Track"] == "OvalTrack") & 
                               (racing["Engine"] == "Bayes"), :]

#%%
# Sort the dataset by "TopSpeedReached" in ascending order
racing_sorted = racing.sort_values(by=['TopSpeedReached'])

# Sort the dataset by "TopSpeedReached" in ascending order and then by 
# "FinishTime" in descending order.
racing_sorted2 = racing.sort_values(by=['TopSpeedReached', 'FinishTime'],
                                    ascending=[True, False])

#%%
# Remove the "TopSpeedReached" column
racing_2 = racing.drop("TopSpeedReached", axis = 1)

# Remove the last 10 observations
racing_reduced = racing[:-10]

#%%
# Create a new variable in the racing dataset called "CheckPoint1to2" 
# which will contain the time it took to go from checkpoint 1 to  
# checkpoint 2.
racing["CheckPoint1to2"] = racing["CheckPoint2"] - racing["CheckPoint1"]

#%%
#The variable "CheckPoint2_66" contains a 1 if checkpoint 2 was passed 
# within the first 66% of the completed race time  and a value of 0 if 
# this is not the case.
# Recode this variable to contain the words "yes" and "no"

# Create a dictionary
to_replace = {1 : "Yes",
              0 : "No"}
#change the 1s and 0s to a new column to CheckPoint2_66_change, 
#as i dont wanna override which is dangerous
racing["CheckPoint2_66_change"] = racing["CheckPoint2_66"].replace(to_replace)

#%%
# Create a new variable in the racing data set based on the "FinishTime" variable"
# If FinishTime > 25, the new variable display "slow"
# If FinishTime <= 25, the new variable display "fast"

def slow_fast(time):
    if time > 25:
        return "slow"
    else:
        return "fast"
    
racing["Indicator"] = racing["FinishTime"].apply(slow_fast)

#%%
# Print all the duplicated rows
duplicates = racing.duplicated(keep = False)
dups = racing[duplicates]

# Remove the duplicated rows (but one of the rows should be kept in the 
# data frame)

no_dups = racing.drop_duplicates(keep = "first")