from application import db

class Band(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    band_name = db.Column(db.String(70), nullable=False)
    band_email = db.Column(db.String(50), nullable=False)
    band_phone = db.Column(db.Integer(20))
    band_genre = db.Column(db.String(20))
    agent_id = db.Column(db.Integer, db.ForeignKey('Agent.id'), nullable=False)

class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agent_name = db.Column(db.String(70), nullable=False)
    agent_email = db.Column(db.String(50), nullable=False)
    agent_phone = db.Column(db.Integer(20))
    band = db.relationship('Band', backref='agentbr')


    