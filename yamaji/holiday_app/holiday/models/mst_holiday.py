from holiday import db

class Entry(db.Model):
    __tablename__ = 'holiday'
    holi_date = db.Column(db.Date, primary_key = True)
    holi_text = db.Column(db.String(20), unique=True)

    def __init__(self, holi_date= None , holi_text = None):
        self.holi_date = holi_date
        self.holi_text = holi_text

        def __repr__(self):
            return '<Entry holi_date:{} holi_text:{}>'.format(self.holi_date, self.holi_text)