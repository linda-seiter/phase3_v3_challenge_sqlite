from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from model import db, Moon
from views.schema import MoonSchema

blp = Blueprint("Moon API", __name__, description="Operations on moons")


@blp.route("/moons")
class Moons(MethodView):
    @blp.response(200, MoonSchema(many=True))
    def get(self):
        """List moons"""
        return db.session.scalars(db.select(Moon))

    @blp.arguments(MoonSchema)
    @blp.response(201, MoonSchema)
    def post(self, fields):
        """Insert a new moon"""
        moon = Moon(**fields)
        try:
            db.session.add(moon)
            db.session.commit()
        except SQLAlchemyError as err:
            db.session.rollback()
            abort(400, moon=err.__class__.__name__,
                  errors=[str(x) for x in err.args])
        return moon


@blp.route("/moons/<int:moon_id>")
class MoonById(MethodView):
    @blp.response(200, MoonSchema)
    def get(self, moon_id):
        """Get moon by id"""
        return db.get_or_404(Moon, moon_id)

    @blp.response(204)
    def delete(self, moon_id):
        """Delete moon by id"""
        moon = db.get_or_404(Moon, moon_id)
        try:
            db.session.delete(moon)
            db.session.commit()
        except SQLAlchemyError as err:
            db.session.rollback()
            abort(400, moon=err.__class__.__name__,
                  errors=[str(x) for x in err.args])

    @blp.arguments(MoonSchema)
    @blp.response(200, MoonSchema)
    def patch(self, fields, moon_id):
        """Update moon by id"""
        try:
            moon = db.get_or_404(Moon, moon_id)
            for key, value in fields.items():
                setattr(moon, key, value)
            db.session.commit()
        except SQLAlchemyError as err:
            db.session.rollback()
            abort(400, moon=err.__class__.__name__,
                  errors=[str(x) for x in err.args])
        return moon
