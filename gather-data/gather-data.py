from googleapiclient.discovery import build
from csv import writer, reader
import key
import pandas as pd

youtube = build('youtube', 'v3', developerKey=key.key)

# requesting Search API to search for top 10 videos for a given query
request = youtube.search().list(
  part='snippet',
  q='Learn Java',
  maxResults='10'
  )

# storing search api's response in a CSV
response = request.execute()

search_data = []
comments= []
for item in response.get('items', []):
  if not item['id'].get('videoId') == None:
    video_id = item['id'].get('videoId')
  comment_request = youtube.commentThreads().list(
    part='snippet',
    videoId=video_id,
    maxResults=10
  )

  comment_res = comment_request.execute()
  for comment in comment_res.get('items', []):
    comment_data = {
      'kind': comment['kind'],
      'top_comments': comment['snippet'].get('topLevelComment').get('snippet').get('textDisplay')
    }
    comments.append(comment_data)
  video_data = {
    'kind': item['kind'],
    'video_id': item['id'].get('videoId'),
    'channel': item['snippet'].get('channelId'),
    'channel_title': item['snippet'].get('channelTitle'),
    'video_published': item['snippet'].get('publishedAt'),
    'video_title': item['snippet'].get('title'),
    'video_thumbnails': item['snippet'].get('thumbnails'),
    'video_url': item['snippet'].get('url'),
    'comments': comments
  }
  search_data.append(video_data)

df = pd.DataFrame([search_data])
df.to_csv('search_data.csv', index=False)



