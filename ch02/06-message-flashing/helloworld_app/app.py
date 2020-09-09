from flask import Flask, redirect, request, render_template, session, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField



app = Flask(__name__)
app.secret_key = b'b837366d86f5b4e33e1766802a964828'


class LoginForm(FlaskForm):
    username = StringField('Username')
    login = SubmitField('Login')


@app.route("/")
def index():
    if 'username' in session:
        return '''Logged in as <b>%s</b>
                  <br>
                  <a href = "/logout"><p style="text-align:center">To log out click here</p></a>
               ''' % session['username']
    flash("You are on the LOGIN page.")
    return 'You are not logged in. To log in <a href = "/login">click here</a>'


@app.route("/hello/<name>")
@app.route("/hello/")
def hello(name='Microservices'):
    first_name_or_title = request.args.get('name', 'Building')
    return render_template("hello.html", name=first_name_or_title , surname=name)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
