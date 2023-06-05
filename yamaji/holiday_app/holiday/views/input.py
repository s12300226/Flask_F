from flask import request, redirect, url_for, render_template, flash, session
from holiday import app, db
from holiday.models.mst_holiday import Entry

@app.route('/')
def show_entries():
    return render_template('input.html')