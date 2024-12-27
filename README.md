# Youtube Choice Optimizer
The youtube choice optimizer curates and suggests youtube videos that best
fit your learning preferances by analyzing video comments. This program uses
the youtube API to search for videos given a user's query and uses nltk's and
spaCy's natural language processing tools to clean user data and youtube data.
The program then vectorizes comment data per video and user preference data
using sklearn and assigns a cosine similarity score. The user is then delivered
with the top 3 videos that match their learning preferences for the query that
they requested.

This terminal run program's goal is to provide an easy decision making process when it comes to choosing which youtube video to watch. Using NLP and ML tools, the program can match a user's specific needs to top 3 videos based on human feedback such as comments. This allows a user to quicly choose which videos to watch without spending time on videos that might not match their interests.

## main.py
The user is first prompted in the terminal to provide their youtube search query
and their specific learning preferances. Then a request is sent to youtube API
to retrieve the top 10 videos and their comments. The comments are then cleaned
and catagorized. Cleaned comments and user preferences are sent then analyzed
and top 3 choices are returned to the user.

## gather_data.py
A request is made to youtube's 'search' api and 'comment_thread' api to retrieve
user query's search results and each video's comments. The videos and comments
are stored in a dictionary that is then converted into a pandas DataFrame to be
stored in a csv.

## data_cleaning.py
2 functions that clean the comment and user preference data. clean_pref_comments
function is a general text cleaning function that removes stopwords and
tokenizes the given text into a list divided by each word or phrase. It uses
**NLTK**'s **stopwords** and **word_tokenizer** tools to clean and tokenize text. This
function also utlizes **spaCy's** *d*ependency parsing** tool to group similar words
together such as "visual learner" instead of "visual" , "learner. clean_comments
function takes the entire corpus of video and comment data and applies
the clean_pref_comments function to each comment and returns a hashmap of video
title to cleaned comment data.

## choice_analysis.py
top3_analysis function utlizes **sklearn** and it's **CountVectorizer** and
**cosine_similarity** tools to first vectorize comment data and user preference
data. After building the vectors or matricies, it's runs a consine_similarity
calculation and assigns a similarity score to each video. Each video title and its similarity score is stored in a max_heap. At the end of the calculations, the function returns the top 3 videos in a list.
