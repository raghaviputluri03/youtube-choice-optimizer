"""
File Name: main.py
Author: Raghavi Putluri
Created: 12/26/2024

Description: Terminal based program that prompts users for the topic they want
to search for and their learning prefernces. This program fetches the data from
Youtube API, cleans it, and returns the top 3 youtube videos that match given
preferences.
"""
import pandas as pd

from data_cleaning import clean_prefs_comments, clean_comments
from gather_data import request_video
from choice_analysis import top3_analysis


#prompt user for search prompt and learning preferances
query = input("Search Query: ")
user_preferances = input("Your Learning Preferances: ")

#run gather-data
request_video(query)

#run data cleaning
cleaned_prefs = clean_prefs_comments(query)

df = pd.read_csv('data/search_data.csv')
video_to_comments = clean_comments(df)

#run choice_analyis and return top 3 videos
result_arr = top3_analysis(video_to_comments, cleaned_prefs)

print(result_arr)