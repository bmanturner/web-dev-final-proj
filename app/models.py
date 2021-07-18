from flask_login import UserMixin
from datetime import datetime
from . import db

class User(UserMixin, db.Model):
    def __repr__(self):
        return '<User %r>' % self.name
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    reviews = db.relationship('Review', backref='user', order_by='desc(Review.created_date)', lazy=True)


class Review(db.Model):
    def __repr__(self):
        return '<Review %r>' % self.movie_id
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.String(100), nullable=False) # movie api's unique id for a movie
    created_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    rating = db.Column(db.Integer, nullable=False)
    user_review = db.Column(db.String(280), nullable=False) # review text, up to 280 characters