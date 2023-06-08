from game import db
from datetime import datetime

class Ranking(db.Model):
    __tablename__ = 'ranking'
    name = db.Column(db.String(20), primary_key = True)
    score = db.Column(db.Integer)
    play_date = db.Column(db.DateTime)

    def __init__(self, name = None , score = None):
        self.name = name
        self.score = score
        self.created_at = datetime.utcnow()

        def __repr__(self):
            return '<Ranking name:{} score:{}>'.format(self.name, self.score)