from flask import Flask, render_template
import requests
import json

#Länkar våra statiska filer
app = Flask(__name__, static_url_path = "",static_folder = "")

'''Vår startsida'''
@app.route('/')
def index_html():
    return render_template('index.html')

'''Sidan som kommer upp vid sökning av film, med datan'''
@app.route('/movie', methods=['GET'])
def movie_html():

#Våra parametrar som vi vill hämta
    params = {
    "api_key": "bb0755d98c763275608828339b9368b2",
    "query": "",
    "year": "4"
    }

#Hämtar parametrarna genom URL-länken och visas i json
    r = requests.get('https://api.themoviedb.org/3/search/movie', params=params)
    r.json()


    params= {
      "q": "",
      "type": 'video',
      "videoDuration": 'short',
      "videoEmbeddable": 'true',
      "part": 'snippet',
      "maxResults": 3
      }

    r = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
    r.json()

#Returdatan blir en html-sida som heter movie.html med data sparad i variabeln "movie"
    return render_template('movie.html', movie = r)


if __name__ == '__main__':
    app.run(debug = True)
