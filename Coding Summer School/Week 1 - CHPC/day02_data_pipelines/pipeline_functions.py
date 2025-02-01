# -*- coding: utf-8 -*-
"""
Pipeline Functions
"""



"""

"""

# Import pandas
import pandas as pd



def extract(file_path):
    # Read the file into memory
    data = pd.read_csv(file_path)
    
    # Now, print the details about the file
    print(f"Here is a little bit of information about the data stored in {file_path}:")
    print(f"\nThere are {data.shape[0]} rows and {data.shape[1]} columns in this DataFrame.")
    print("\nThe columns in this DataFrame take the following types: ")
    
    # Print the type of each column
    print(data.dtypes)
    
    # Finally, print a message before returning the DataFrame
    print(f"\nTo view the DataFrame extracted from {file_path}, display the value returned by this function!\n\n")
    
    return data
    


def transform(apps, reviews, category, min_rating, min_reviews):
    # Print statement for observability
    print(f"Transforming data to curate a dataset with all {category} apps and their "
          f"corresponding reviews with a rating of at least {min_rating} and "
          f"{min_reviews} reviews\n")
    
    # Drop any duplicates from both DataFrames (also have the option to do this in-place)
    reviews = reviews.drop_duplicates()
    apps = apps.drop_duplicates(["App"])
    
    # Find all of the apps and reviews in the food and drink category
    subset_apps = apps.loc[apps["Category"] == category, :]
    subset_reviews = reviews.loc[reviews["App"].isin(subset_apps["App"]), ["App", "Sentiment_Polarity"]]
    
    # Aggregate the subset_reviews DataFrame
    aggregated_reviews = subset_reviews.groupby(by="App").mean()
    
    # Join it back to the subset_apps table
    joined_apps_reviews = subset_apps.join(aggregated_reviews, on="App", how="left")
    
    # Keep only the needed columns
    filtered_apps_reviews = joined_apps_reviews.loc[:, ["App", "Rating", "Reviews", "Installs", "Sentiment_Polarity"]]
    
    # Convert reviews, keep only values with an average rating of at least 4 stars, and at least 1000 reviews
    filtered_apps_reviews = filtered_apps_reviews.astype({"Reviews": "int32"})
    top_apps = filtered_apps_reviews.loc[(filtered_apps_reviews["Rating"] > min_rating) & (filtered_apps_reviews["Reviews"] > min_reviews), :]
    
    # Sort the top apps, replace NaN with 0, reset the index (drop, inplace)
    top_apps.sort_values(by=["Rating", "Reviews"], ascending=False, inplace=True)
    top_apps.reset_index(drop=True, inplace=True)
     
    # Persist this DataFrame as top_apps.csv file
    top_apps.to_csv("top_apps.csv")
    
    print(f"The transformed DataFrame, which includes {top_apps.shape[0]} rows "
          f"and {top_apps.shape[1]} columns has been persisted, and will now be "
          f"returned")
    
    # Return the transformed DataFrame
    return top_apps


import sqlite3

# Now, create a function to do this
def load(dataframe, database_name, table_name):
    # Create a connection object
    con = sqlite3.connect(database_name)
    
    # Write the data to the specified table (table_name)
    dataframe.to_sql(name=table_name, con=con, if_exists="replace", index=False)
    print("Original DataFrame has been loaded to sqlite\n")
    
    # Read the data, and return the result (it is to be used)
    loaded_dataframe = pd.read_sql(sql=f"SELECT * FROM {table_name}", con=con)
    print("The loaded DataFrame has been read from sqlite for validation\n")
    
    try:
        assert dataframe.shape == loaded_dataframe.shape
        print(f"Success! The data in the {table_name} table have successfully been "
              f"loaded and validated")

    except AssertionError:
        print("DataFrame shape is not consistent before and after loading. Take a closer look!")


