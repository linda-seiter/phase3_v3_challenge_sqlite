from setup import db


class Planet(db.Model):
    """Planet model"""
    __tablename__ = "planets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    distance_from_sun = db.Column(db.Integer)

    moons = db.relationship(
        'Moon', back_populates="planet", cascade='all, delete-orphan')


class Moon(db.Model):
    """Moon model"""
    __tablename__ = "moons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    orbital_period = db.Column(db.Float)

    planet_id = db.Column(db.Integer, db.ForeignKey(
        'planets.id'), nullable=False)

    planet = db.relationship('Planet', back_populates='moons')
