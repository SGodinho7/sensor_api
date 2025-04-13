from app.app import db


class Sensor(db.Model):
    __tablename__ = 'sensor'

    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    desc = db.Column(db.String(200))
    state = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'{self.sid}, {self.name}, {self.desc}, {self.state};'

    @property
    def serialize(self):
        return {
            'sid': self.sid,
            'name': self.name,
            'desc': self.desc,
            'state': self.state,
        }
