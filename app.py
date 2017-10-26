
from flask import Flask, render_template
import requests

app = Flask(__name__, static_url_path = "",static_folder = "")



@app.route('/')
def index_html():
    return render_template('index.html')


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
