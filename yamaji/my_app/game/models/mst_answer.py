from game import db
from datetime import datetime

class Answer(db.Model):
    __tablename__ = 'answers'
    id = db.Column(db.Integer, primary_key = True)
    answer = db.Column(db.String(4))
    hit = db.Column(db.Integer)
    blow = db.Column(db.Integer)

    def __init__(self, id = None , answer = None, hit = None, blow = None):
        self.id = id
        self.answer = answer
        self.hit = hit
        self.blow = blow

        def __repr__(self):
            return '<Answer id:{} answer:{} hit:{} blow:{}>'.format(self.id, self.answer, self.hit, self.blow)