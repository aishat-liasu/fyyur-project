from email.policy import default
from app import db
from datetime import datetime
from sqlalchemy.dialects import postgresql

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String)
    genres = db.Column(postgresql.ARRAY(db.String))
    seeking_for_artist = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String)
    artists = db.relationship('Artist', secondary='Show', backref=db.backref('venues', lazy=True), viewonly=True)
    shows = db.relationship('Show', backref='venues', lazy=True)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String)
    genres = db.Column(postgresql.ARRAY(db.String))
    seeking_for_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String)
    #venues = db.relationship('Venue', backref=db.backref('artists', lazy=True)) 
    shows = db.relationship('Show', backref='artists',lazy=True)

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Show(db.Model):
    __tablename__ = 'Show'

    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.now())

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

