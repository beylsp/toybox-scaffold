import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    {%- if cookiecutter.use_db == "yes" %}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    {%- endif %}

class DevelopmentConfig(Config):
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY") or "development"
    {%- if cookiecutter.use_db == "yes" %}
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEV_DATABASE_URL") or \
        "sqlite:///" + os.path.join(basedir, "sqlite.db")
    {%- endif %}

config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig,
}