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
    content_filter = ""

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
    pass
    # move on
else:
    pass
    # handle error
    #credits to Tenor for template. URL for template here: https://tenor.com/gifapi/documentation?gclid=EAIaIQobChMIw8HPp-7T5AIVdBh9Ch3Xmw2fEAAYASACEgJFEvD_BwE#quickstart
    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html")

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
    if r.status_code == 200:
        return render_template("index.html")
    
    
if __name__ == '__main__':
    app.run(debug=True)
