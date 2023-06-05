from flask_blog import db
from datetime import datetime

"""
ログインユーザーテーブル作成プログラム
"""

class User(db.Model):
    __tablename__ ='blog_users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))


    def __init__(self, username, password):
        self.username = username
        self.password = password


    def __repr__(self):
        return'f<User id:{self.id} title:{self.username} text:{self.password}'
    