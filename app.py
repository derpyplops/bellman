from flask import Flask, render_template, request
from gevent.pywsgi import WSGIServer
import settings as settings

import json


app = Flask(__name__)
app.secret_key = settings.SECRET_KEY


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/q")
def query():
    page = request.args.get("page")
    if page == "home":
        data = json.loads(open(settings.HOME_DATA, "r").read())
    return json.dumps(data)


http_server = WSGIServer(("", settings.PORT), app)
http_server.serve_forever()
