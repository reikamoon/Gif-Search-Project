from flask import Flask, render_template, request
import requests
import json
from random import choice

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""

    apikey = "KWIISY5DIB57"
    limit = 10
    search_term = request.args.get("search")
    content_filter = "high"


    params = {
        "query" : search_term,
        "key" : apikey,
        "limit" : limit,
        "content_filter" : content_filter
    }

    # Use the query, api key, and limit to find a gif
    r = requests.get("https://api.tenor.com/v1/search?q=%s&KWIISY5DIB57=%s&10=%s" % (search_term, apikey, limit))

    if r.status_code == 200:
        gifs = json.loads(r.content)["results"]
    # move on
    else:
        gifs = "None"


    return render_template("index.html", gifs=gifs, search=search_term)
#Trending function, will use the apikey and limit to show the trending gifs.
@app.route('/trending')
def trending():
    """Return Trending Gifs"""
    apikey = "KWIISY5DIB57"
    limit = 10
    content_filter = "high"

    params = {
        'key': apikey,
        'limit': limit,
        'content_filter': content_filter
    }
    r = requests.get("https://api.tenor.com/v1/trending?key=%s&limit=%s" % (apikey, limit))
    if r.status_code == 200:
        gifs = json.loads(r.content)["results"]
    else:
        gifs = None

    return render_template("index.html")
#Random function. Will display random gifs.
@app.route('/random')
def random():
    """Give random gifs"""
    apikey = "KWIISY5DIB57"
    limit = 10
    content_filter = "high"

    params = {
        'key': apikey,
        'limit': limit,
        'content_filter': content_filter
    }

    r = requests.get("https://api.tenor.com/v1/trending_terms?key=%s" % (apikey,))
    if t.status_code == 200:  # If the request was successful
        term_list = json.loads(t.content)["results"]
    else:
        term_list = None

    search = choice(term_list)

    # Make add random query term to params
    params['q'] = search

    r = requests.get("https://api.tenor.com/v1/random?q=%s&key=%s&limit=%s" % (search_term, apikey, lmt))

    if r.status_code == 200:  # If the request was successful
        gifs = json.loads(r.content)["results"]
    else:
        gifs = None

    return render_template("index.html", gifs=gifs, search=search)


if __name__ == '__main__':
    app.run(debug=True)
