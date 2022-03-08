from flask import Flask
{%- if cookiecutter.use_db == "yes" %}
from flask_sqlalchemy import SQLAlchemy
{%- endif %}

from config import config
from webapp.context import base_context

{%- if cookiecutter.use_db == "yes" %}
db  = SQLAlchemy()
{%- endif %}

def create_app(config_name):
    app = Flask(
        __name__,
        static_folder="../static",
        template_folder="../templates"
    )
    app.config.from_object(config[config_name])
    app.context_processor(base_context)

    {%- if cookiecutter.use_db == "yes" %}
    db.init_app(app)
    {%- endif %}

    from webapp.routes import ui_blueprint
    app.register_blueprint(ui_blueprint)

    return app