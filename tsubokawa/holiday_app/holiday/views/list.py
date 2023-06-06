from holiday import app
from flask import request, redirect, url_for, render_template, flash
from holiday.models.holidays import Holiday
from holiday import db


@app.route('/list')
def show_holidays():
    """
    祝日のリストを表示する処理
    """
    # holidaysにはDB内の全ての祝日のデータが入っている
    holidays = Holiday.query.order_by(Holiday.holi_date.asc()).all()
    return render_template('list.html', holidays=holidays)