from flask import Flask, jsonify, request
import csv

all_articles = []

with open('shared_articles.csv',encoding = 'utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

liked_article = []
not_liked_article = []
did_not_watch = []

app = Flask(__name__)

@app.route('/get-article')
def get_article():
    return jsonify({
        'data':all_articles[0],
        'status':'success'
    })

@app.route('/liked_article', methods = ['POST'])
def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_article.append(article)
    return jsonify({
        'status':'success'
    }),201

@app.route('/not_liked_article', methods = ['POST'])
def not_liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_article.append(article)
    return jsonify({
        'status':'success'
    }),201

@app.route('/did_not_watch_article', methods = ['POST'])
def did_not_watch():
    article = all_articles[0]
    all_articles = all_articles[1:]
    did_not_watch.append(article)
    return jsonify({
        'status':'success'
    }),201
if __name__ == '__main__':
    app.run()