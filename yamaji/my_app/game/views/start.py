from flask import request, redirect, url_for, render_template, flash, session
from game import app, db
from game.models.mst_ranking import Ranking
from game.models.mst_answer import Answer
from game.date.make_seaclet_answer import make_answer, add_user_name
from functools import wraps

# def login_required(view):
#     @wraps(view)
#     def innner(*arg, **kwargs):
#         if not session.get('logged_in'):
#             return redirect(url_for('login'))
#         return view(*arg, **kwargs)
#     return innner


# @login_required
@app.route('/')
def show_title():
    ranking = Ranking.query.order_by(Ranking.score.asc()).all()
    return render_template('title.html', ranking=ranking)


# ゲームのスタート処理
@app.route('/start', methods=['GET', 'POST'])
def start_game():

    if request.form['username'] == '':
        flash('名前を入力してください')
        return redirect(url_for('show_title'))
    elif len(request.form['username']) > 20:
        flash('名前は20文字以内で入力してださい')
        return redirect(url_for('show_title'))

    make_answer()
    delete_log()
    add_user_name(request.form['username'])
    return redirect(url_for('game'))


# ゲーム終了時に回答DBをクリア
def delete_log():
    answers = Answer.query.all()
    for answer in answers:
        db.session.delete(answer)
        db.session.commit()
    return