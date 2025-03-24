from app.app import db


class Sensor(db.Model):
    __tablename__ = 'sensor'

    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text)
    state = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.sid}, {self.name}, {self.desc}, {self.state};'
