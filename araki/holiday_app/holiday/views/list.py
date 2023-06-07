from holiday import app
from flask import request, redirect, url_for, render_template, flash
from holiday.models.mst_holiday import Entry
from holiday import db

#データベースからデータの一覧取得
@app.route('/list')
def show_list():
    holidays = Entry.query.order_by(Entry.holidate.asc()).all()
    return render_template('list.html', holidays=holidays)