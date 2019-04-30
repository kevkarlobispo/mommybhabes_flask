from flask import render_template, request, Blueprint
from flask_1.models import Recipe

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    # recipes = Recipe.query.all()
    page = request.args.get('page', 1, type=int)
    recipes = Recipe.query.order_by(Recipe.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', recipes=recipes)


@main.route("/about")
def about():
    return render_template('about.html', title='About')


