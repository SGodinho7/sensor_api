import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db_type = os.getenv('WEB_DB', 'sqlite')
if db_type == 'postgresql':
    user = os.getenv('PG_USER')
    password = os.getenv('PG_PASSWORD')
    ip = os.getenv('PG_IP')
    port = os.getenv('PG_PORT', '5432')
    database_name = os.getenv('PG_DATABASE')
    schema = os.getenv('PG_SCHEMA', 'public')

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates')
    if db_type == 'postgresql':
        app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{
            ip}:{port}/{database_name}?options=-c%20search_path={schema}'
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db.sqlite'

    db.init_app(app)

    # import blueprints here
    from app.blueprints.core.routes import core
    from app.blueprints.sensor_api.routes import sensors

    app.register_blueprint(core, url_prefix='/')
    app.register_blueprint(sensors, url_prefix='/sensors')

    migrate = Migrate(app, db)

    return app
