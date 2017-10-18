# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
app = Flask(__name__, static_url_path = "",static_folder = "")

@app.route('/')
def index_html():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)
