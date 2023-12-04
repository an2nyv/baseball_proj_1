import pandas as pd
import os

#Changes the working directory
new_dirr = "/Users/Anthony Vallejo/OneDrive/Desktop/Personal_Projects/DATA/baseballData"
os.chdir(new_dirr)

current_directory = os.getcwd()
print(current_directory)

battingData = pd.read_csv('Batting.csv')
masterData = pd.read_csv('Master.csv')

#Working with data from the latest expansion era (1998)
battingData.yearID.astype('int32')
battingData['yearID'] = pd.to_datetime(battingData.yearID, format="%Y")
battingData = battingData.loc[battingData['yearID'] > '1997']
battingData['yearID'] = battingData['yearID'].dt.year


