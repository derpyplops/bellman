from flask import Flask, render_template, request
from gevent.pywsgi import WSGIServer
import settings as settings


app = Flask(__name__)
app.secret_key = settings.SECRET_KEY


@app.route("/")
def home():
    return "Hello world"


http_server = WSGIServer(("", settings.PORT), app)
http_server.serve_forever()
