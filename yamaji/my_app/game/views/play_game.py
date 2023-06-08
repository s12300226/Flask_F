from flask import request, redirect, url_for, render_template, flash, session
from game import app, db
from game.models.mst_answer import Answer
from game.models.mst_ranking import Ranking
import game.date.seaclet_answer as g


# ゲームページのメイン画面処理
@app.route('/game', methods=['GET', 'POST'])
def game():
    answer = Answer.query.order_by(Answer.id.desc()).all()
    return render_template('game.html', answers=answer)


# ゲーム画面の入力処理
@app.route('/game/answer', methods=['GET', 'POST'])
def input_value():

    input_val_str = [request.form['val1'], request.form['val2'], request.form['val3'], request.form['val4']]
    if varidate(input_val_str):
         flash("異なる4つの数字を入力してください")
         return redirect(url_for('game'))
    
    input_val = [int(request.form['val1']), int(request.form['val2']), int(request.form['val3']), int(request.form['val4'])]
    
    ans_val = [g.val1, g.val2, g.val3, g.val4]
    
    # プレイヤーの回答の精査
    hit, blow = game(input_val, ans_val)
    # DBに登録
    answer_val = request.form['val1'] + request.form['val2'] + request.form['val3'] + request.form['val4']
    id = Answer.query.count() + 1
    entry_answer(id, answer_val, hit, blow)

    if hit == 4:
        answer = Answer.query.order_by(Answer.id.desc()).all()
        return render_template('gameclear.html', answers=answer)

    return redirect(url_for('game'))

# ゲームクリアの処理
@app.route('/game/clear', methods=['GET'])
def game_clear():
    entry_ranking(g.username, Answer.query.count())
    return redirect(url_for('show_title'))

# ゲーム画面の終了処理
@app.route('/end', methods=['GET'])
def finish_game():
    return redirect(url_for('show_title'))

# ゲームをあきらめる処理
@app.route('/game/gameover', methods=['GET'])
def game_over():
    ans_val = [g.val1, g.val2, g.val3, g.val4]
    return render_template('gameover.html', ans_val=ans_val)


# hit and blow 機能の実装
def game(input_value, ans_value):
    hit_num = 0
    blow_num = 0

    for i in range(4):
        if input_value[i] == ans_value[i]:
            hit_num += 1
        else:
            pass

    for j in input_value:
        if j in ans_value:
            blow_num += 1
        else:
            pass
    blow_num = blow_num - hit_num

    return hit_num, blow_num


# 回答をデータベースに保存する
def entry_answer(id, answer_val, hit, blow):
    answer = Answer(
        id=id,
        answer=answer_val,
        hit=hit,
        blow=blow,
    )
    db.session.add(answer)
    db.session.commit()
    return


# 回答をデータベースに保存する
def entry_ranking(user_name, score):
    
    ranking = Ranking(
        name = user_name,
        score = score
    )
    db.session.add(ranking)
    db.session.commit()
    return


def varidate(input_value_str):

    for val_str in input_value_str:
        if val_str == '':
            return True

    return False