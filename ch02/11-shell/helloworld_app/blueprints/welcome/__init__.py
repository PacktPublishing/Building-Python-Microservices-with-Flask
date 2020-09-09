from flask import Blueprint, request, render_template

welcome_bp = Blueprint('welcome', __name__, url_prefix='/welcome', template_folder='templates', static_folder='static')

@welcome_bp.route("/")
def welcome():
    first_name_or_title  = request.args.get('name', '')
    return render_template("welcome/index.html", name=first_name_or_title)
