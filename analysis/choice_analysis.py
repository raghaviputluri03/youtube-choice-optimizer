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


def top3_analysis(video_to_comments, cleaned_prefs):
  """
    Vectorizes comment data and preference data. Uses cosine similarity to
    calculate the similarities between each video's comments compared to user
    preferences. Stores video title and rating on a max heap, returns the top
    3 videos with most similarity.

    Parameters
    ----------
    video_to_comments: dict with video titles mapping to it's comments
    user_prefs: cleaned array of user preferences

    Returns
    -------
    list[]
        top 3 vidoes in relevance to user prefernces.
  """
  video_to_rating = []
  result_arr = []

  pref_arr = " ".join(cleaned_prefs)

  #instance of CountVectorizer
  vectorizer = CountVectorizer()

  for video, comments in video_to_comments.items():
    comments_arr = " ".join(comments)

    # fit_transform: fit creates a vocabulary of all unique words
    # fit_transform: transform: creates a numerical matrix
      # -> each row is a sentence and each column is a word in the vocab
      # -> matrix shows the number of times a word appears in each sentence
    comments_vectors = vectorizer.fit_transform([comments_arr])
    user_input_vector = vectorizer.transform([pref_arr])

    # calculates cosinse similarity between the user's input vector (matrix) against
      # each of the matricies or vectors formed by the sentences in the original data
      # results in an array containing the similarity scores per data sentence
    similarity_scores = cosine_similarity(user_input_vector, comments_vectors)

    #creating a max_heap using negative sign to switch the order of min heap
    heapq.heappush(video_to_rating, (-similarity_scores, video))

  # returning the top 3 videos
  for _ in range(3):
    result_arr.append(heapq.heappop(video_to_rating)[1])

  return result_arr


