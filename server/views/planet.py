from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from model import db, Planet
from views.schema import PlanetSchema

blp = Blueprint("Planet API", __name__, description="Operations on planets")


@blp.route("/planets")
class Planets(MethodView):

    @blp.response(200, PlanetSchema(many=True))
    def get(self):
        """List planets"""
        return db.session.scalars(db.select(Planet))

    @blp.arguments(PlanetSchema)
    @blp.response(201, PlanetSchema)
    def post(self, fields):
        """Insert a new planet"""
        planet = Planet(**fields)
        try:
            db.session.add(planet)
            db.session.commit()
        except SQLAlchemyError as err:
            db.session.rollback()
            abort(400, planet=err.__class__.__name__,
                  errors=[str(x) for x in err.args])
        return planet


@blp.route("/planets/<int:planet_id>")
class PlanetsById(MethodView):

    @blp.response(200, PlanetSchema)
    def get(self, planet_id):
        """Get planet by id"""
        return db.get_or_404(Planet, planet_id)

    @blp.response(204)
    def delete(self, planet_id):
        """Delete planet by id"""
        planet = db.get_or_404(Planet, planet_id)
        try:
            db.session.delete(planet)
            db.session.commit()
        except SQLAlchemyError as err:
            db.session.rollback()
            abort(400, planet=err.__class__.__name__,
                  errors=[str(x) for x in err.args])

    @blp.arguments(PlanetSchema)
    @blp.response(200, PlanetSchema)
    def patch(self, fields, planet_id):
        """Update planet by id"""
        planet = db.get_or_404(Planet, planet_id)
        for key, value in fields.items():
            setattr(planet, key, value)
        try:
            db.session.commit()
        except SQLAlchemyError as err:
            db.session.rollback()
            abort(400, planet=err.__class__.__name__,
                  errors=[str(x) for x in err.args])
        return planet
