#!venv/bin/python
"""Run script for the app."""
from app import app as application

if __name__ == "__main__":
    application.run(debug=app.config["DEBUG"])
