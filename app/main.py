from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from .models import User, Review
import requests
from . import db, movie_api_key

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
    if len(search_text) == 0:
        return render_template('movies.html')
    resp = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={movie_api_key}&query={search_text}")
    results = resp.json()['results']

    return render_template('movies.html', results=results, search_text=search_text)

@main.route('/movies/<movie_id>', methods=['GET'])
@login_required
def movie(movie_id):
    # TODO: retrieve movie data from external API
    # TODO: retrieve all movie reviews from database
    # from .models import Review
    # reviews = Review.query.filter_by(movie_id=movie_id)
    resp = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={movie_api_key}")
    reviews = Review.query.filter_by(movie_id=movie_id).all()
    for review in reviews:
        print(review.user.name)
        print(review.rating)
        print(review.movie_title)
    movie = resp.json()

    return render_template('review.html', movie_id=movie_id, reviews=reviews, movie=movie)

@main.route('/movies/<movie_id>', methods=['POST'])
@login_required
def add_review(movie_id):
    # TODO: add a new review. see auth.signup for code example
    rating = request.form['options']
    review_text = request.form.get('review_text')
    title = request.form.get('movie_title')
    new_review = Review(user_id=current_user.id, rating=rating, review_text=review_text, movie_id=movie_id, movie_title=title)
    db.session.add(new_review)
    db.session.commit()
    print(new_review)
    return redirect(f"/movies/{movie_id}")
