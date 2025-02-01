# -*- coding: utf-8 -*-
"""
What I have:
    
star_wars!1977&Lucas.mp4

What I want:
Star Wars (1977) - Lucas.mp4

Other options:
    - list comprehension
    - regex

import logging instead of print
add try and except

how can you improve

some files were not renamed properly

- git updates...


"""

import os
import shutil
import sys

# ------------------ v3 -------------------
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("file_renamer.log"),
        logging.StreamHandler()
    ]
)

logging.info(f"\n***************PROCESSING - DATA***************")



# ------------- v2 ------------------
skipped_movies = []

# Define the directory containing the messy files
source_directory = "./messy_movie_files"
new_directory = "./renamed_movie_files"

# Ensure the directory exists
if not os.path.exists(source_directory):
    logging.error("Source directory not found! Exiting...")
    # print("Directory not found!")
    sys.exit()  # Replace exit() with sys.exit()
    
# Ensure the new directory exists, if not create it
if not os.path.exists(new_directory):
    logging.info(f"Created new directory: {new_directory}")
    os.makedirs(new_directory)

# Function to normalize file names
def normalize_filename(filename):
    # Remove the file extension
    
    try:
        name, ext = os.path.splitext(filename)
        # print("*******************************************************")
        # print(f"Processing file: {filename}, Name: {name}, Extension: {ext}")
        logging.info(f"Processing file: {filename}")
    
        # # Replace common separators with spaces
        # name = name.replace("_", " ").replace("-", " ").replace(";", " ").replace("!", " ").replace("@", " ")
        # print(f"After replacing separators: {name}")
        
            # Replace common separators with spaces
        for sep in ["_", "-", ";", "!", "@", "&", ",", "."]:
            name = name.replace(sep, " ")
        logging.debug(f"After replacing separators: {name}")
        
        # # Replace underscore with space
        # name = name.replace("_", " ")
        # print(f"After replacing underscores: {name}")
        
        # # Replace hyphen with space
        # name = name.replace("-", " ")
        # print(f"After replacing hyphens: {name}")
        
        # # Replace semicolon with space
        # name = name.replace(";", " ")
        # print(f"After replacing semicolons: {name}")
        
        # # Replace exclamation mark with space
        # name = name.replace("!", " ")
        # print(f"After replacing exclamation marks: {name}")
        
        # # Replace at symbol with space
        # name = name.replace("@", " ")
        # print(f"After replacing at symbols: {name}")    
        
        # # ----------- v2 -----------------
            
        # # Replace and symbol with space
        # name = name.replace("&", " ")
        # print(f"After replacing at symbols: {name}")    
        
        # # Replace comma symbol with space
        # name = name.replace(",", " ")
        # print(f"After replacing at symbols: {name}")    
        
        # # Replace dot symbol with space
        # name = name.replace(".", " ")
        # print(f"After replacing at symbols: {name}")    
        
    
        # Split into parts (words)
        parts = name.split()
        # print(f"Parts after splitting: {parts}")
        logging.debug(f"Parts after splitting: {parts}")
    
    
        # Find the year (4 digits)
        year = None
        for part in parts:
            if part.isdigit() and len(part) == 4:
                year = part
                # print(f"Year found: {year}")
                logging.warning(f"No valid year found for file: {filename}")
                break
    
        # If no year is found, skip the file
        if not year:
            print(f"Skipping: {filename} (no valid year found)")
            # ------------- v2 ------------------
            skipped_movies.append(filename)
            return None
    
        # Get the movie title (everything before the year)
        title_parts = parts[:parts.index(year)]
        movie_title = " ".join(title_parts).strip().title()
        # print(f"Movie title: {movie_title}")
    
        # Get the director (everything after the year)
        director_parts = parts[parts.index(year) + 1:]
        director = " ".join(director_parts).strip().title() if director_parts else "Unknown"
        # print(f"Director: {director}")
    
        # Format the new file name
        new_name = f"{movie_title} ({year}) - {director}{ext}"
        # print(f"New name generated: {new_name}")
        logging.info(f"New name generated: {new_name}")
        return new_name
    
    except Exception as e:
        logging.error(f"Error processing file {filename}: {e}")
        skipped_movies.append(filename)
        return None

# Process files in the source directory
for filename in os.listdir(source_directory):
    old_path = os.path.join(source_directory, filename)
    if not os.path.isfile(old_path):
        continue  # Skip directories or non-files

    new_name = normalize_filename(filename)
    if not new_name:
        print(f"Skipping: {filename} (no match)")
        continue

    # Define the new path in the new directory
    new_path = os.path.join(new_directory, new_name)

    # Copy the file to the new directory with the new name
    shutil.copy(old_path, new_path)
    print(f"Copied and renamed: {filename} -> {new_name}")

print("Renaming and moving complete!")
# ------------- v2 ------------------
print(skipped_movies)

# Count files in the source directory
source_files = os.listdir(source_directory)
source_file_count = len(source_files)
print(f"Number of files in source directory '{source_directory}': {source_file_count}")

# Count files in the new directory (if it exists)
if os.path.exists(new_directory):
    new_files = os.listdir(new_directory)
    new_file_count = len(new_files)
    print(f"Number of files in new directory '{new_directory}': {new_file_count}")
else:
    print(f"The new directory '{new_directory}' does not exist.")
