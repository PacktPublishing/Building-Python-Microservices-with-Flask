from flask import Flask, redirect, request, render_template, session, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask_sqlalchemy import SQLAlchemy
from .greeting import greet_bp
from .blueprints.welcome import welcome_bp

app = Flask(__name__)
app.secret_key = b'b837366d86f5b4e33e1766802a964828'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test1.db'
app.register_blueprint(greet_bp)
app.register_blueprint(welcome_bp)
db = SQLAlchemy(app)


def check_uniqueness(form, user):
    if Users.query.filter(Users.username == user.data).first():
        raise ValidationError("User already exists.")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        check_uniqueness
    ])
    login = SubmitField('Login', validators=[DataRequired()])


class Users(db.Model):
    username = db.Column(db.String(128), primary_key=True, unique=True, nullable=False)


db.create_all()


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
    app.logger.debug("Rendering with name %s, surname %s", first_name_or_title, name)
    return render_template("hello.html", name=first_name_or_title , surname=name)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    message = None
    if not form.validate():
        message = "Please enter a username never entered before."
    elif request.method == 'POST':
        session['username'] = request.form['username']
        user = Users(username=session['username'])
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("login.html", message=message, form=form)


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
