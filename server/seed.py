
from app import app
from sqlalchemy import delete

from models import Planet, Moon
from setup import db


def seed():
    """Seed tables"""

    # delete all rows
    db.session.execute(delete(Moon))
    db.session.execute(delete(Planet))

    mercury = Planet(name="Mercury", distance_from_sun=35000000)
    venus = Planet(name="Venus", distance_from_sun=67000000)
    earth = Planet(name="Earth", distance_from_sun=93000000)
    mars = Planet(name="Mars", distance_from_sun=142000000)
    db.session.add_all([mercury, venus, earth, mars])
    db.session.commit()

    db.session.add(Moon(name="Moon", orbital_period=27.3, planet_id=earth.id))
    db.session.add(Moon(name="Phobos", orbital_period=0.3, planet_id=mars.id))
    db.session.add(Moon(name="Deimos", orbital_period=1.4, planet_id=mars.id))
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        seed()
