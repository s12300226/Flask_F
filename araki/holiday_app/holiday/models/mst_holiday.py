from holiday import db

class Entry(db.Model):
    __tablename__ ='holiday'
    holidate = db.Column(db.Date, primary_key=True)
    holi_text = db.Column(db.String(20))

def __init__(self, holidate, holi_text):
    self.holidate = holidate
    self.holi_text = holi_text
