"""
モンスターテーブルを作成するプログラム
"""

from pokemon import db

class Monster(db.Model):
    __tablename__ = 'monster'
    id = db.Column(db.Integer, primary_key=True)
    mons_name = db.Column(db.String(50))
    mons_hp = db.Column(db.Integer)
    mons_atc = db.Column(db.Integer)
    pos = db.Column(db.String(20))
    catch_per = db.Column(db.Integer)
    is_catched = db.Column(db.String(10))

    def __init__(self):
        self.id = db.session.query(Monster).count() + 1
