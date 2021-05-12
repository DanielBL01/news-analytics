from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Result(db.Model):
    __tablename__ = 'results'
    
    id = db.Column(db.Integer, primary_key = True)
    url = db.Column(db.String(), unique = True, nullable = False)
    sentiment = db.Column(db.String(15), nullable = False)
    summary = db.Column(db.String(), unique = True, nullable = False)
    mcommon = db.Column(db.String(45))
    licommon = db.Column(db.String())