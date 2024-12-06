# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 21:14:23 2024

@author: Gary
"""

import pandas as pd

# Read data from the text file, assuming space separation
try:
  data = pd.read_csv('data.txt', delimiter=' ', header=None)
except FileNotFoundError:
  print("Error: 'data.txt' not found. Please upload the file or provide the correct path.")
  exit()

# Write the data to an Excel file
try:
  data.to_excel('output.xlsx', index=False, header=False) #index=False to avoid writing row index, header=False to avoid writing column names
  print("Data successfully written to output.xlsx")
except Exception as e:
  print(f"An error occurred while writing to the Excel file: {e}")
