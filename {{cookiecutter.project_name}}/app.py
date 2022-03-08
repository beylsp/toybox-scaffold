import click
import flask
import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

{%- if cookiecutter.use_db == "yes" %}
from flask_migrate import Migrate, upgrade

from webapp.app import create_app, db


app = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)


@app.teardown_appcontext
def remove_db_session(response):
    db.session.remove()
    return response


@app.cli.command()
def deploy():
    """Run deployment tasks"""
    # migrate database to latest revision
    upgrade()
{%- else %}
from webapp.app import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "default")


@app.cli.command()
def your_command():
    """Run your command"""
    pass
{%- endif %}