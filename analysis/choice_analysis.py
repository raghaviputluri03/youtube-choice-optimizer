"""
File Name: choice_analysis.py
Author: Raghavi Putluri
Created: 12/17/2024
Description: Inputs youtube's top 10 video reccomendations for a given topic
and analyzes the top 3 videos that would be the most useful for a user given
their specific learning preferances based on comments. Therefore users can
be more confident in knowing which videos to watch that fit their needs.
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import heapq

from data_cleaning import video_to_comments
from data_cleaning import cleaned_prefs

video_to_rating = []
result_arr = []

pref_arr = " ".join(cleaned_prefs)

vectorizer = CountVectorizer()

for video, comments in video_to_comments.items():
  comments_arr = " ".join(comments)

  comments_vectors = vectorizer.fit_transform([comments_arr])
  user_input_vector = vectorizer.transform([pref_arr])

  similarity_scores = cosine_similarity(user_input_vector, comments_vectors)

  heapq.heappush(video_to_rating, (-similarity_scores, video))

for _ in range(3):
  result_arr.append(heapq.heappop(video_to_rating)[1])

print(result_arr)


