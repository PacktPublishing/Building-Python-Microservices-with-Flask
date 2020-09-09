from flask import Flask, redirect, request, render_template, session, url_for


app = Flask(__name__)
app.secret_key = b'b837366d86f5b4e33e1766802a964828'


@app.route("/")
def index():
    if 'username' in session:
        return '''Logged in as <b>%s</b>
                  <br>
                  <a href = "/logout"><p style="text-align:center">To log out click here</p></a>
               ''' % session['username']
    return 'You are not logged in. To log in <a href = "/login">click here</a>'


@app.route("/hello/<name>")
@app.route("/hello/")
def hello(name='Microservices'):
    first_name_or_title = request.args.get('name', 'Building')
    return render_template("hello.html", name=first_name_or_title , surname=name)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return """
            <form action = "" method = "POST">
                <label for="username">Username</label>
                <p><input type = text id = "username" name = username placeholder="ex. bruce_wayne" required></p>
                <p><input type = submit value = Login></p>
            </form>
            """

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


#with app.test_request_context():
    #print("Exercise 1:" + url_for('hello', dummy_qp='non_existent'))
    #print("Exercise 2:" + url_for('hello', name='wayne', dummy_qp='non_existent'))
    #print("Exercise 3:" + url_for('hello', name='wayne', name='bruce'))
