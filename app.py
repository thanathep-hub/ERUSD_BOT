import json

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/webhook')
def webhook():
     return 'this is webhook url'