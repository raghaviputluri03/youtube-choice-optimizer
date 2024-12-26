"""
File Name: choice_analysis.py
Author: Raghavi Putluri
Created: 12/17/2024
Description: Inputs user preferences and youtube video comments and
pre-processess them getting rid of unecessary words and grouping similar
words together to send to analysis.
"""
import csv
import pandas as pd
import nltk
import spacy
import pprint as pp

nltk.download('stopwords')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nlp = spacy.load("en_core_web_sm") #spaCy lang model tools for dependency parsing

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag

df = pd.read_csv('data/search_data.csv')
stop_words = set(stopwords.words('english'))

cleaned_prefs = []
vc_dict = {}
video_to_comments = {}


user_pref = """I am a visual learner who likes examples and learn best through
              hands-on learning"""


def clean_prefs_comments(text):
    """
    Cleans given text by removing stop and filter words. Tokenizes
    preferences into a list divided by each word

    Parameters
    ----------
    user_pref: user preference blurb provided by the user

    Returns
    -------
    list[]
        cleaned and tokenized preferences divided by each preference string
    """
    #remove stop words: I, a, the, who, and etc. using nltk stopwords
    # tokens = word_tokenize(user_pref)
    # pref_tokens = pos_tag(tokens)
    pref_tokens = word_tokenize(text)
    filtered_prefs = [w for w in pref_tokens if not w.lower() in stop_words]

    #combine verbs and noun
    #figure this out

    #combine similar words: 'visual', 'learner' to 'visual learner using spaCy
    #dependecy parsing
    modified_text = " ".join(filtered_prefs).replace("-", "_")
    doc = nlp(modified_text)

    combined_prefs = []
    for token in doc:
        combined_prefs.append(token.text)
        if token.dep_ in ['compound', 'amod']: #if token is a compound or adjective modifier
            combined_prefs.append(token.text + ' ' + token.head.text) #put the token and it's head together
            #NOTE: remove 'learning' and other head words?
    return combined_prefs

# cleaning user_preferences
cleaned_prefs = clean_prefs_comments(user_pref)

# Iterate through each row and clean comments
for index, row in df.iterrows():
    cleaned_comments = clean_prefs_comments(row['comments'])
    video_to_comments[row['video_title']] = cleaned_comments

#store cleaned data into csv
    with open('data/cleaned_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(['video_title', 'comment'])

        for video_title, comments in video_to_comments.items():
            for comment in comments:
                writer.writerow([video_title, comment])
