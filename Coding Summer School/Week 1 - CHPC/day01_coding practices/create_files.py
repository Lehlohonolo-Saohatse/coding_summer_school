# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 09:24:03 2024

@author: BBarsch
"""

import os

# Define the directory for messy files
directory = "./messy_movie_files"

# Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# List of messy movie file names to create
messy_files = [
    "Inception--2010--Nolan.mp4",
    "THE-GODFATHER_1972_Ford.avi",
    "star_wars!1977&Lucas.avi",
    "Harry-Potter-2001.Rowling.mp4",
    "AVATAR!2009_Cameron.mp4",
    "Dark_Knight;2008!Nolan.mp4",
    "Titanic_1997-Cameron.avi",
    "matrix-1999&wachowski.mp4",
    "Shawshank-Redemption;1994,Robbins.avi",
    "Forrest_Gump-1994.TomHanks.avi",
    "Gladiator;2000_Ridley!Scott.mp4",
    "Lord_of_Rings-2003-Jackson.mp4",
    "Pulp-Fiction_1994_Tarantino.avi",
    "Interstellar--2014--Nolan.mp4",
    "Back;ToTheFuture;1985;Spielberg.avi",
    "The_Lion!King!1994;Disney.flv",
    "Frozen-2013_Disney.mp4",
    "Pirates!of_the-Caribbean-2003-Verbinski.mp4",
    "Jurassic;Park-1993-Spielberg.flv",
    "The_Avengers;2012-Whedon.mp4"
]

# Create the messy files in the specified directory
for filename in messy_files:
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as file:
        file.write("")  # Create an empty file

print(f"Created {len(messy_files)} messy files in {directory}!")
