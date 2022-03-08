from flask import Blueprint
from flask.globals import request
import flask

from webapp.views import (
    hello,
)


ui_blueprint = Blueprint("ui_blueprint", __name__, url_prefix="/")


# Routes
# ===

@ui_blueprint.route("/")
def home():
    return flask.render_template("index.html")

ui_blueprint.add_url_rule("/hello/<string:name>", view_func=hello)

