from application import db

class Band(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band_name = db.Column(db.String(70), nullable=False)
    band_email = db.Column(db.String(50), nullable=False)
    band_phone = db.Column(db.Integer(20))
    