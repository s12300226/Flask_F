"""
違法駐車の居場所と画像の投稿データを管理する
「reporsテーブル」を作成するプログラム
"""

from car_report import db
from datetime import datetime
import requests



class Report(db.Model):
    __tablename__ = 'reports'
    username = db.Column(db.String(20), primary_key=True)
    report_date = db.Column(db.DateTime, primary_key=True)
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    file_name = db.Column(db.String(100))

    def __init__(self,username,file_name):
        self.username = username
        self.report_date = datetime.utcnow()
        geo_request_url = 'https://get.geojs.io/v1/ip/geo.json'
        data = requests.get(geo_request_url).json()
        self.lat = data['latitude']
        self.lon = data['longitude']
        self.file_name = file_name



