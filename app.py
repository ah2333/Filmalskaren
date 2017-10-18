# -*- coding: utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route("/")
def index_html():
    return render_template('index_html')
