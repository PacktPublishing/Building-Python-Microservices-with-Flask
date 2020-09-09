from flask import Flask, request


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route("/hello/<name>")
@app.route("/hello/")
def hello(name='Microservices'):
    first_name_or_title = request.args.get('name', 'Building')
    return "Hello, %s %s" % (first_name_or_title, name)
