from __init__ import app, db
from flask_sqlalchemy import SQLAlchemy

class FourDichotomy(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(200), nullable = False)
    description = db.Column(db.String(200), nullable = False)
    initial = db.Column(db.String(10), nullable = True )

    def __repr__(self):
        return '<Personality Type %r>' % self.type

class PersonalityTypes(db.Model):

    ptype = db.Column(db.String(200), primary_key = True)
    characteristics = db.Column(db.Text(500), nullable = False)
    how_other_sees_them = db.Column(db.Text(500), nullable = False)
    areas_of_growth = db.Column(db.Text(500), nullable = False)
    keywords = db.Column(db.String(20), nullable = False)

    def __repr__(self):
        return '<Personality Name %r>' % self.ptype

class Facts(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    facts = db.Column(db.String(200), nullable = False)

    def __repr__(self):
        return '<fact name %r>' %self.facts