import pandas as pd
import os

new_dirr = "/Users/Anthony Vallejo/OneDrive/Desktop/Personal_Projects/DATA/baseballData"

os.chdir(new_dirr)

current_directory = os.getcwd()
print(current_directory)

battingData = pd.read_csv('Batting.csv')

