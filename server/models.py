from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata=MetaData(naming_convention={
    'pk': 'pk_%(table_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'ix': 'ix_%(table_name)s_%(column_0_name)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
})

db = SQLAlchemy(metadata=metadata)

class Planet(db.Model):
    """Planet model"""
    __tablename__ = "planets"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    distance_from_sun = db.Column(db.Integer, nullable=False)
    moons = db.relationship(
        "Moon", back_populates="planet", cascade="all, delete-orphan")
    
class Moon(db.Model):
    """Moon model"""
    __tablename__ = "moons"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    orbital_period = db.Column(db.Float, nullable=False)

    planet_id = db.Column(db.Integer, db.ForeignKey("planets.id"), nullable=False)
    planet = db.relationship("Planet", back_populates="moons")
