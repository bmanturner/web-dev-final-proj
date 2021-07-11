# Movie Review Site

## Requirements

1. Python 3.8
2. `pipenv`

## Installation

1. `pipenv install`

## Initial Set-up (also done after wiping db)

1. Enter pipenv shell (`pipenv shell`)
2. Enter python repl (`python`)
3. `>>> from app import db, create_app`
4. `>>> db.create_all(app=create_app())`
5. `>>> quit()`

## Starting Application

1. Enter pipenv shell (`pipenv shell`)
2. `python server.py`
3. Open browser to `http://localhost:5000`

## Dependency Documentation

1. [Flask](https://flask.palletsprojects.com/en/2.0.x/)
2. [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
3. [Bootstrap](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

### Next Steps

1. Implement movie search (`main.search_movies`) with an external movie API using the [requests](https://docs.python-requests.org/en/latest/user/quickstart/) python package
2. Display results of movie search, clicking on a movie to bring you to movie page.
3. Movie page: Fetch and display data for an individual movie (`main.movie`)
4. Display form on movie page to review movie if user hasn't already reviewed the movie (post data to `main.add_review`)
5. Display reviews on user profile page
6. Display top ten movies (by average rating) on home page
7. Display 3 most recent movie reviews on home page
