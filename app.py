from flask import Flask, render_template, request
import requests
import json
from random import choice

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""

    apikey = "KWIISY5DIB57"
    lmt = 10
    search_term = request.args.get("search")
    content_filter = "high"
    
    params = {
        "query" : search_term,
        "key" : apikey,
        "limit" : lmt,
        "content_filter" : filter
    }


    r = requests.get("https://api.tenor.com/v1/search", params=params)

    if r.status_code == 200:
        first_gifs = json.loads(r.content)["results"]
    # move on
    else:
        first_gifs = "None"


    return render_template("index.html", first_gifs=first_gifs, search=search_term)

@app.route('/trending')
def trending():
    """Return Trednging Gifs"""
    apikey = "KWIISY5DIB57"
    limit = 10
    content_filter = "high"

    params = {
        'key': apikey,
        'limit': limit,
        'content_filter': filter
    }
    r = requests.get("https://api.tenor.com/v1/trending", params=params)
    if r.status_code == 200:
        first_gifs = json.loads(r.content)["results"]
    else:
        first_gifs = None

    return render_template("index.html")


@app.route('/random')
def random():
    """Give random gifs"""
    apikey = "KWIISY5DIB57"
    limit = 10
    content_filter = "high"

    params = {
        'key': apikey,
        'limit': limit,
        'content_filter': filter
    }

    t = requests.get("https://api.tenor.com/v1/trending_terms", params=params)
    if t.status_code == 200:  # If the request was successful
        term_list = json.loads(t.content)["results"]
    else:
        term_list = None

    search = choice(term_list)

    # Make add random query term to params
    params['q'] = search

    r = requests.get("https://api.tenor.com/v1/random", params=params)
    
    if r.status_code == 200:  # If the request was successful
        first_gifs = json.loads(r.content)["results"]
    else:
        first_gifs = None

    return render_template("index.html", first_gifs=first_gifs, search=search)


if __name__ == '__main__':
    app.run(debug=True)
