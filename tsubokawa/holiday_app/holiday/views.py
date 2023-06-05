from holiday import app
from flask import request, redirect, url_for, render_template, flash, session
from holiday.models.holidays import Holiday
from holiday import db

@app.route('/')
def home():
    return render_template('input.html')


@app.route('/show')
def show_holidays():
    holidays = Holiday.query.order_by(Holiday.holi_date.desc()).all()
    return render_template('show.html', holidays=holidays)