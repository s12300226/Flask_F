"""
マスタユーザー情報を管理するテーブルを作成するプログラム
"""

from car_report import db
import requests

class Mst_Report(db.Model):
    __tablename__ = 'report_mst'
    #マスタのid
    mst_id = db.Column(db.Integer, primary_key=True)
    mst_name = db.Column(db.String(50))
    mst_pass = db.Column(db.String(50))

def __init__(self,mst_name,mst_pass):
    #idは連番
    self.mst_id = db.session.query(Mst_Report).count() + 1
    self.mst_name = mst_name
    self.mst_pass = mst_pass
    