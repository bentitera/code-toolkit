import flask
from flask import render_template

app = flask.Flask(__name__)

# ------HERE IS MY MODEL--------#
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('data/yelp.csv')


@app.route('/')
def is_good():
    food = flask.request.args['text']
    ans = df[df.text.str.contains(food)].nlargest(10, 'stars')
    rev = ans.text
    return render_template('view.html', tables = [a.to_html()])


if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = '4000'
    app.run(HOST, PORT)
