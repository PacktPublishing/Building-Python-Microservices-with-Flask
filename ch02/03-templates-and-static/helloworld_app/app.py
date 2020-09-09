from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("hello.html", name="World!", surname=None)


@app.route("/hello/<name>")
@app.route("/hello/")
def hello(name='Microservices'):
    first_name_or_title = request.args.get('name', 'Building')
    return render_template("hello.html", name=first_name_or_title , surname=name)
