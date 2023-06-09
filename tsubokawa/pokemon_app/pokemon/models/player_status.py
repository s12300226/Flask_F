"""
プレイヤーステータステーブルを作成するプログラム
"""

from pokemon import db

class PlayerStatus(db.Model):
    __tablename__ = 'user_status'
    id = db.Column(db.Integer, primary_key=True)
    pos_ver = db.Column(db.Integer)
    pos_hor = db.Column(db.Integer)
    hp = db.Column(db.Integer)
    atc = db.Column(db.Integer)
    level = db.Column(db.Integer)

    def __init__(self):
        self.id = db.session.query(PlayerStatus).count() + 1
        # プレイヤーの初期位置を登録
        # 基本はデータを更新する
        self.pos_ver = 180
        self.por_hor = 240
        self.hp = 250
        self.atc = 100
        self.level = 1
