from flask import Flask, render_template, request
import requests
import json


app = Flask(__name__, static_url_path = "",static_folder = "")

@app.route('/movie', methods=['POST'])
def movie_():
    search = request.form['search']
    r = requests.get('http://www.omdbapi.com/?t=' +search+ '&apikey=a7e52ea9')
    movies = r.json()
    trailer_key = trailer_(movies)
    return render_template('movie.html', trailer_key=trailer_key, movies = movies)

def trailer_(movies):
    search = request.form['search']
    trailer = search + 'official%20trailer'
    r = requests.get('https://www.googleapis.com/youtube/v3/search?key=AIzaSyBVpfQAOe4tdWlAsp4GTM0fCBtYwfYvqXY&q=' +trailer+movies['Year']+'&type=video&videoDuration=any&videoEmbaddable=true&part=snippet&maxResults=1&videoDefinition=high')
    data = json.loads(r.text)
    for item in data['items']:
        items = ((item['id']))
        trailer_key = ((items['videoId']))
        return trailer_key


@app.route('/')
def index_html():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug = True)

