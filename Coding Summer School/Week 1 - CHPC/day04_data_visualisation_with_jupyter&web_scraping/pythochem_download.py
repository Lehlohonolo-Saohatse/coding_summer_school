# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:45:58 2025

@author: user-pc
"""

import requests as req
import os

# Create a folder for the bioact
try:
    os.mkdir("bioact")
except FileExistsError:
    pass

# Define the URL of the .gov webpage
base = 'https://phytochem.nal.usda.gov'

# Change range according to first and last entry of webpage search
for bio in range(1, 6):
    compurl = "/biological-activities-chemicals-csv-export/"+str(bio)+"/all?page&_format=csv"
    if os.path.isfile("bioact/"+str(bio)+".csv"):
        print(str(bio)+" already downloaded")
    else:
        # Send a GET request to the webpage
        res = req.get(base+compurl)
        csv = open("bioact/"+str(bio)+".csv","wb")
        csv.write(res.content)
        csv.close()
        print("Downloading "+str(bio))

# Download compounds from pubchem
import pubchempy as pcp
import pandas as pd
import glob
from pandas.errors import EmptyDataError

# Create a folder for sdf files
try:
    os.mkdir("SDFS")
except FileExistsError:
    pass

# Find all the csv files and store in an array
csv_files = []
# Specify subdirectory that contain csv files and store all csv filenames
csv_files += (glob.glob("bioact\*.csv"))

lig = []
# Read data from csv files and store in temp dataframe
for files in csv_files:
    try:
        temp_df = pd.read_csv(files, sep=',')
        lig.append(temp_df)
    except EmptyDataError:
        print(files+" is an empty csv file")

# Combine all data into single dataframe
df = pd.concat(lig, axis=0, ignore_index=True)

tot = [] 

# Iterate through names in dataframe
for name in df['Chemical Name']:
    # Search for the chemical on PubChem
        compounds = pcp.get_compounds(name, 'name')
        # Check for CID for each compound
        for compound in compounds:
            cid = compound.cid
        # Download SDF files based on CID
        # Also note if you write out files based on name and not CID you will only end 
        # up with the last SDF instead of various hits that are found for the name
            pcp.download('SDF', 'SDFS/'+str(cid)+'.sdf', cid, 'cid', overwrite=True)
            print("Downloading "+str(cid))
            tot.append(cid)

print("Total number of SDFs downloaded: "+str(len(tot)))
print('DONE')

