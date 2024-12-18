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

#learn sentimental analysis/preference matching beginner's version
    """
    idea: go through each comment, clean up filter words like "the, and, you"
            etc. and then see if the learning preferences of users matches any of
            the comment's. Keep a count per video and videos with the 3 highest
            counts of matching words from comments are returned
                - maybe use sentiment analysis to find how well they match
                the preferance words?
                (easiest but might take long?)
                - start with NLTK and Scikit-learn to pre-process text
                    - removing stop words
                - go into TF-IDF Vectorizer and cosine similarity to rank
                  matches between user preferences and comments
    """
# map out how it can work for this project
    """
    step 1: tokenize user preferences into a list and pre-process (today)
    step 2: pre-process comments (remove stopwords, filter words, emojis) (today)

    step 3: check if comments match preference words
              - if yes: increase pref_counter of each video by # and store
    step 4: gather counts for all videos, sort the videos by count, and take the
    first 3
    step 5: return first 3
    """

#rate each video's data
    #add to a top three array




#go through each video, note down it's title and go through comments
#Rating Criteria:
#--> Comments match user preferences as close as possible:
