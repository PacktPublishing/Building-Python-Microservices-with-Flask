from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/hello/<name>")
@app.route("/hello/")
def hello(name='Microservices'):
    return "Hello, %s" % name
