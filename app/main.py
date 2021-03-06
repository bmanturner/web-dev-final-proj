from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, current_user
from .models import User, Review
import requests
from sqlalchemy import func, desc
from . import db, movie_api_key

main = Blueprint('main', __name__)

@main.route('/')
def index():
    recent = Review.query.order_by(Review.created_date.desc()).limit(5)

    top_10 = db.session.query(
        Review.movie_id,
        Review.movie_title,
        func.avg(Review.rating).label('average')
    ).group_by(Review.movie_id).order_by(desc('average')).limit(10).all()

    return render_template('index.html', recent=recent, top_10=top_10)

@main.route('/profile')
@login_required
def profile():
    reviews = Review.query.filter_by(user_id=current_user.id).all()
    return render_template('profile.html', name=current_user.name, reviews=reviews)

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
    resp = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={movie_api_key}")
    reviews = Review.query.filter_by(movie_id=movie_id).order_by(Review.created_date.desc()).limit(5).all()

    user_has_reviewed = any(review.user.id == current_user.id for review in reviews)

    movie = resp.json()

    return render_template('review.html', movie_id=movie_id, reviews=reviews, movie=movie, user_has_reviewed=user_has_reviewed)

@main.route('/movies/<movie_id>', methods=['POST'])
@login_required
def add_review(movie_id):
    rating = request.form['options']
    review_text = request.form.get('review_text')
    title = request.form.get('movie_title')

    new_review = Review(user_id=current_user.id, rating=rating, review_text=review_text, movie_id=movie_id, movie_title=title)
    db.session.add(new_review)
    db.session.commit()

    return redirect(f"/movies/{movie_id}")
