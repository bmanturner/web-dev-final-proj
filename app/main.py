from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    # TODO: query database to retrieve the top ten movies as determined by the average review rating
    # TODO: BONUS: add the most recent ___ reviews entered on the site
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    # TODO: query database to retrieve a list of movies reviewed by the current logged in user

    return render_template('profile.html', name=current_user.name, movies=[])

@main.route('/movies', methods=['GET', 'POST'])
@login_required
def search_movies():
    if request.method == 'GET':
        return render_template('movies.html')

    search_text = request.form.get('search_text')
    # TODO: run search with search_text, return any data that may be useful on the frontend
    # such as: img url, unique identifier, year...

    results = [{ 'title': 'The Thing' }, { 'title': 'The Hills Have Eyes' }] # mocked results

    return render_template('movies.html', results=results, search_text=search_text)

@main.route('/movies/<movie_id>', methods=['GET'])
@login_required
def movie(movie_id):
    # TODO: retrieve movie data from external API
    # TODO: retrieve all movie reviews from database
    # from .models import Review
    # reviews = Review.query.filter_by(movie_id=movie_id)
    return 'Movie Page'

@main.route('/review', methods=['POST'])
@login_required
def add_review():
    # TODO: add a new review. see auth.signup for code example
    return 'Review Not Added! Still to be Implemented!'
