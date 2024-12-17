"""
File Name: choice_analysis.py
Author: Raghavi Putluri
Created: 12/17/2024
Description: Inputs youtube's top 10 video reccomendations for a given topic
and analysis the top 3 videos that would be the most useful for a user given
their specific learning preferances based on comments therefore users can
be more confident in knowing which videos to watch.
"""
import csv
import pandas as pd

user_preferences = ["visual learner", "hands-on learning" , "likes examples"]

df = pd.read_csv('gather-data/search_data.csv')

# Iterate through each row
for index, row in df.iterrows():
    print(row)
    #each row you go through comments and match learning preferances to the comments
    #add a rating to each row
    #at the end return the top 3 ratings

# learn sentimental analysis beginner's version (watch 1 video)
# map out how it can work for this project

#rate each video's data
    #add to a top three array




#go through each video, note down it's title and go through comments
#Rating Criteria:
#--> Comments match user preferences as close as possible:
