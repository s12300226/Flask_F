"""
違法駐車の居場所と画像の投稿データを管理する
「reporsテーブル」を作成するプログラム
"""

from car_report import db
from datetime import datetime
import requests



class Report(db.Model):
    __tablename__ = 'reports'
    # id(連番, primary_key)
    id = db.Column(db.Integer, primary_key=True)
    # ユーザー名
    username = db.Column(db.String(20))
    # 通報日時
    report_date = db.Column(db.DateTime)
    # 通報位置情報
    # 緯度
    lat = db.Column(db.Float)
    # 経度
    lon = db.Column(db.Float)
    # 画像ファイル名
    file_name = db.Column(db.String(100))
    # 備考
    text = db.Column(db.Text)
    # 対応状況（未対応か対応済みか）
    status = db.Column(db.String(10))

    def __init__(self,username,file_name,text,status='未対応'):
        # 連番なのでデータ数+1をidとする
        self.id = db.session.query(Report).count() + 1
        self.username = username
        self.report_date = datetime.now()
        geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
        data = requests.get(geo_request_url).json()
        self.lat = data['latitude']
        self.lon = data['longitude']
        self.file_name = file_name
        self.text = text
        self.status = status
        



