from marshmallow import Schema, fields
from marshmallow.validate import Length, Range


class MoonSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=Length(
        min=1, error="Must not be empty string."))
    orbital_period = fields.Float(required=True, validate=Range(min=0))
    planet_id = fields.Int(required=True)
    planet = fields.Nested(lambda: PlanetSchema(exclude=("moons",)), dump_only=True)

    
class PlanetSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=Length(
        min=1, error="Must not be empty string."))
    distance_from_sun = fields.Int(required=True, validate=Range(min=0))
    moons = fields.List(fields.Nested(MoonSchema(exclude=("planet",))), dump_only=True)
