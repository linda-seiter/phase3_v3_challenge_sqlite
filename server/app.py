#!/usr/bin/env python3

from flask import Flask, redirect
from flask_migrate import Migrate
from flask_smorest import Api

from models import db
from default_config import DefaultConfig
from views.planet import blp as PlanetBlueprint
from views.moon import blp as MoonBlueprint

app = Flask(__name__)
app.config.from_object(DefaultConfig)
app.json.compact = False

Migrate(app, db)
db.init_app(app)

api = Api(app)
api.register_blueprint(PlanetBlueprint)
api.register_blueprint(MoonBlueprint)


@app.route('/')
def index():
    return redirect(app.config["OPENAPI_SWAGGER_UI_PATH"])


if __name__ == '__main__':
    app.run(port=5555, debug=True)
