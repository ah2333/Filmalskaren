<<<<<<< HEAD
=======
import argparse
>>>>>>> origin/master

from flask import Flask, render_template, request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
app = Flask(__name__, static_url_path = "",static_folder = "")

DEVELOPER_KEY = 'AIzaSyBR8d23Es_KgpAqNFDDdPFRYZsk2Z5jKWo'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(methods = 'GET'):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    filmalskarenKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    q = 'surfing',
    part = 'snippet, id',
    maxResults = 1,
    type = ''
  ).execute()

  videos = []
  title = []

  for search_result in search_response.get('title', 'videos', []):
    if search_result["id"]['kind'] == 'youtube#video':
      videos.append('%s (%s)' % (search_result['snippet']['title'],
                                 search_result['id']['videoId']))
    elif search_result["id"]["kind"] == "youtube#title":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["titleId"]))

  print('Videos:\n' , '\n'.join(videos), '\n')



if __name__ == '__main__':
  search = argparse.ArgumentParser()
  search.add_argument('--q', help='Search term', default='Google')
  search.add_argument('--max-results', help='Max results', default=2)
  args = search.parse_args()

  try:
    youtube_search(args)
  except:
      HttpError

print('An HTTP error')





@app.route('/')
def index_html():
    return render_template('index.html')
<<<<<<< HEAD

params= {
"api_key": "AIzaSyBR8d23Es_KgpAqNFDDdPFRYZsk2Z5jKWo",
"q": "",
"type": "video",
"videoDuration": "short",
"videoEmbeddable": "true",
"part": "snippet",
"maxResults": "3"
}

r = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
print(r.text)








if __name__ == '__main__':
    app.run(debug = True)
=======
>>>>>>> origin/master
