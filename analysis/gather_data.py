from googleapiclient.discovery import build
from csv import writer, reader
import key
import pandas as pd

youtube = build('youtube', 'v3', developerKey=key.key)

def request_video(query):
  # requesting Search API to search for top 10 videos for a given query
  request = youtube.search().list(
    part='id,snippet',
    q=query,
    maxResults='10',
    type='video'
    )

  response = request.execute()

  search_data = []
  #Sending a request to fetch top comments on each video
  for item in response.get('items', []):
    if item['id']['kind'] == 'youtube#video':
      video_id = item['id']['videoId']
    comment_request = youtube.commentThreads().list(
      part="snippet",
      videoId=video_id,
      textFormat="plainText"
    )



  #storing video data into a dict per video
    comment_res = comment_request.execute()
    comments= []
    for comment in comment_res.get('items', []):
      comment_obj = comment["snippet"]["topLevelComment"]
      comment_text = comment_obj["snippet"]["textDisplay"]
      comments.append(comment_text)

      video_data = {
        #'kind': item['kind'],
        'video_id': item['id'].get('videoId'),
        'channel_title': item['snippet'].get('channelTitle'),
        'video_published': item['snippet'].get('publishedAt'),
        'video_title': item['snippet'].get('title'),
        #'video_thumbnails': item['snippet'].get('thumbnails'), #use thumbnail to rate
        'video_url': item['snippet'].get('url'),
        'comments': comments
      }
      video_title = item['snippet'].get('title')
    search_data.append(video_data)

  #converting dict into a dataframe and exporting to a csv
  df = pd.DataFrame(search_data)
  df.to_csv('data/search_data.csv', index=False)


