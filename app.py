import os
from flask import Flask
import urllib.request

app = Flask(__name__)

url = os.getenv('URL', "it20.info")

@app.route("/")
def get_url():
    with urllib.request.urlopen('http://' + url) as response:
        html = response.read()
    return html

if __name__ == '__main__':
   app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
   app.debug =True