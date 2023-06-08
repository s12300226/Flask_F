from holiday import app
from flask import request, redirect, url_for, render_template, flash, session

@app.route('/')
def show_entries():
    return render_template('input.html')

@app.route('/blank')
def blank_entry():
    return render_template('blank.html')