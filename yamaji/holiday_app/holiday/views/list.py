from flask import request, redirect, url_for, render_template, flash, session
from holiday import app, db
from holiday.models.mst_holiday import Entry

@app.route('/list', methods=['GET'])
def out_list():
    entries = Entry.query.order_by(Entry.holi_date.asc()).all()
    return render_template('list.html', entries=entries)