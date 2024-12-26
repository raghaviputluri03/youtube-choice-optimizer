"""
File Name: choice_analysis.py
Author: Raghavi Putluri
Created: 12/17/2024
Description: Inputs youtube's top 10 video reccomendations for a given topic
and analyzes the top 3 videos that would be the most useful for a user given
their specific learning preferances based on comments. Therefore users can
be more confident in knowing which videos to watch that fit their needs.
"""
from data_cleaning import video_to_comments
from data_cleaning import cleaned_prefs

print(video_to_comments['Learn Java in 14 Minutes (seriously)'])