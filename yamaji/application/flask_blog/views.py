from flask import request, url_for, render_template, flash, session
from flask_blog import app

@app.route('/')
def show_entries():
    return render_template("entries/index.html")