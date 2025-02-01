# -*- coding: utf-8 -*-
"""
Data Pipeline for ETL

In this code-along, we'll focus on extracting data from flat-files. 
A flat file might be something like a .csv or a .json file. 
The two files that we'll be extracting data from are the apps_data.csv and 
the review_data.csv file. To do this, we'll used pandas. Let's take a closer look!

"""

# Import Pandas



# Ingest these datasets into memory using read_csv and save as apps and reviews variable


# Take peak at the two data sets with print function or view in variable explorer


# View the columns, shape and data types of the data sets

# Is there a single pandas method that does this?

"""
The code above works perfectly well, but this time let's try using DRY-principles to build a function to extract data.

Create a function called extract, with a single parameter of name file_path.
Sprint the number of rows and columns in the DataFrame, as well as the data type of each column. Provide instructions about how to use the value that will eventually be returned by this function.
Return the variable data.
Call the extract function twice, once passing in the apps_data.csv file path, and another time with the review_data.csv file path. Output the first few rows of the apps_data DataFrame.

Extracting is one of the most tricky things to do in a data pipeline, always try to know much as you can about the source system, here its just a flat file which is quite simple.
"""

# Extract Function

    # Read the file into memory
    
    # Now, print the details about the file
    
    # Print the type of each column
    
    # Finally, print a message before returning the DataFrame


# Call the function (create apps_data and reviews_data)

# Take a peek at one of the DataFrames


"""
We have extracted the data and now we want to transform them. 
Now we are going to use the food and drink category. 
So we are going to write a function that provides a top apps view for food and drink. 
So we will write a function that takes in 5 parameters, drop some duplicates
find positive reviews and filter columns. Then only keep a few columns. 
Then join it by min_rating and min_reviews, order it and check for min rating 
of 4 stars with at least 1000 reviews.

"""


# Transform Function

    # Print statement for observability
    
    # Drop any duplicates from both DataFrames (also have the option to do this in-place)
    
    # Find all of the apps and reviews in the food and drink category
    
    # Aggregate the subset_reviews DataFrame
    
    # Join it back to the subset_apps table
    
    # Keep only the needed columns
    
    # Convert reviews, keep only values with an average rating of at least 4 stars, and at least 1000 reviews
    
    # Sort the top apps, replace NaN with 0, reset the index (drop, inplace)
    
    # Persist this DataFrame as top_apps.csv file
    
    # Print what has happened so far
    
    # Return the transformed DataFrame
    
# Call the function

# Show the data




"""
Ok so last step is to load data, now you can save and keep it as csv but for it is 
a better practice to load it into sqlite DB or similar if its quite a large file.
...what advantages are there of loading into a SQL DB?
"""

# Import sqlite

# Load Function

    # Create a connection object
    
    # Write the data to the specified table (table_name)
    
    # Read the data, and return the result (it is to be used)
    
    # Add try/except to handle error handling and assert to check for conditions
    
# Call the function
    
    
    
    
    
    
    