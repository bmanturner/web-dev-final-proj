from app import create_app

# HELPERS
def format_datetime(value, format="%d %b %Y %I:%M %p"):
    """Format a date time to (Default): d Mon YYYY HH:MM P"""
    if value is None:
        return ""
    return value.strftime(format)

if __name__ == "__main__":
  app = create_app()
  app.jinja_env.filters['formatdatetime'] = format_datetime
  app.run(debug=True, use_reloader=True)
