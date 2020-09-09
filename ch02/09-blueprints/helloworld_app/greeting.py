from flask import Blueprint, request, render_template

greet_bp = Blueprint('greet', __name__, url_prefix='/greeting')

@greet_bp.route("/")
def greet():
    first_name_or_title  = request.args.get('name', '')
    return render_template("greeting.html", name=first_name_or_title)
