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

        # TODO: Extract query term from url

        # TODO: Make 'params' dict with query term and API key
    params = {
        "query" : search_term,
        "key" : apikey,
        "limit" : lmt,
        "content_filter" : filter
    }

        # TODO: Make an API call to Tenor using the 'requests' library
            #API CODE FOR TENOR: KWIISY5DIB57
    # set the apikey
    apikey = "KWIISY5DIB57"  # test value

    # get the GIF's id and search used
    shard_gifs_id = top_8gifs[0]["id"]

    search_term = "excited"

    r = requests.get("https://api.tenor.com/v1/search", params=params)

    if r.status_code == 200:
        first_gifs = json.loads(r.content)["results"]
        pass
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

    r = requests.get("https://api.tenor.com/v1/trending_terms", params=params)
    if r.status_code == 200:
        first_gifs = json.loads(r.content)["results"]
    else:
        first_gifs = None

        return render_template("index.html", first_gifs=first_gifs, search=search)


if __name__ == '__main__':
    app.run(debug=True)
