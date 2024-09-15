import pandas as pd
import os

#  'C:\\Users\\Maroof\\Desktop\\Project 1 (1)\\10 Players Bio\\Afghanistan_Cricketers.csv'

data_path = os.getenv('DATA_PATH', 'C:\\Users\\Maroof\\Desktop\\Project 1 (1)')

file_path = os.path.join(data_path, 'Players Ranking', 'odi_all-rounder.csv')

odi_all_rounder=pd.read_csv(file_path)

print(odi_all_rounder)