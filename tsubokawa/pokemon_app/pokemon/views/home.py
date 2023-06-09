from pokemon import app
from flask import request, redirect, url_for, render_template, flash, session
from pokemon import db
from pokemon.models.player_status import PlayerStatus
import os
from pokemon.models.monster import Monster



@app.route('/')
def home():
    # セッション情報を渡す
    # player_l = session['player_left']
    # player_r = session['player_top']
    # print(f'プレイヤーの左位置です:{player_l}')
    print(app.config['POS_VER'])
    return render_template('index.html', playerLeft=240, playerTop=180)

@app.route('/battle/<int:playerLeft>/<int:playerTop>')
def battle(playerLeft,playerTop):
    print('##################')
    print(playerLeft)
    # sessionにプレイヤー位置を保存
    session['player_left'] = playerLeft
    session['player_top'] = playerTop
    monster_pos = '草むら'

    # 生息地が草むらのmonsterを取得
    monster_appered = db.session.query(Monster).filter(Monster.pos=='草むら').first()
    player_status = db.session.query(PlayerStatus).filter(PlayerStatus.id==1).first()

    print('出てきたモンスターは...')
    print(monster_appered.mons_name)

    playerPos = [playerLeft, playerTop]
    return render_template('battle.html', playerPos=playerPos, monster=monster_appered, player=player_status)

@app.route('/escape')
def escape():
    """
    逃げた後の処理ではプレイヤーの位置情報を所持してindex.htmlへ
    """
    playerLeft = session['player_left']
    playerTop = session['player_top']
    print(f'逃げた後は左:{playerLeft}上{playerTop}')
    return render_template('index.html', playerLeft=playerLeft, playerTop=playerTop)


@app.route('/choice_check/<int:id>', methods=['POST'])
def choice_check(id):
    if request.form['choice'] == 'escape':
        return redirect(url_for('escape'))
    elif request.form['choice'] == 'battle':
        monster_status = db.session.query(Monster).filter(Monster.id==id).first()
        player_status = db.session.query(PlayerStatus).filter(PlayerStatus.id==1).first()
        monster_status.mons_hp -= player_status.atc
        player_status.hp -= monster_status.mons_atc
        # monster_hp -= player_status.atc
        # player_hp -= monster_status.atc
        return render_template('battle.html', monster=monster_status, player=player_status)