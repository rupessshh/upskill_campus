import string
import random
from flask import Flask, redirect, request

app = Flask(__name__)

class URLShortener:
    def __init__(self):
        self.url_mapping = {}  # Dictionary to store original and shortened URLs

    def generate_short_url(self, long_url):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(6))  # Generate a 6-character short URL
        self.url_mapping[short_url] = long_url
        return short_url

    def get_original_url(self, short_url):
        return self.url_mapping.get(short_url, None)

url_shortener = URLShortener()

@app.route("/", methods=["GET", "POST"])
def shorten_url():
    if request.method == "POST":
        long_url = request.form["long_url"]
        short_url = url_shortener.generate_short_url(long_url)
        return f"Shortened URL: {request.host_url}{short_url}"

    return '''URL Shortner Project
    
    <form method="post">
    Enter the URL to shorten: <input type="text" name="long_url">
    <input type="submit" value="Shorten">
    </form>

    Made By- Rupesh Khanzode
    '''

@app.route("/<short_url>", methods=["GET"])
def redirect_to_original_url(short_url):
    original_url = url_shortener.get_original_url(short_url)
    if original_url:
        return redirect(original_url)
    else:
        return "Shortened URL not found.", 404

if __name__ == "__main__":
    app.run()
