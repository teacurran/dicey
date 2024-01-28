import inspect
import pkgutil

# Flask Imports
from flask_session import Session, SqlAlchemySessionInterface
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import Flask
from flask_socketio import SocketIO

# Importing configs
from sqlalchemy.ext.declarative import declarative_base

from config import EnvironmentConfig
from app import models

# Setup

# We iniate the database and other packages that are going to play together
# with the app here

# For the database
db = SQLAlchemy()
# For database migrations
# migrate = Migrate()
# For HTML bootstrapping
bootstrap = Bootstrap()

app = Flask(__name__)

socketio = SocketIO(app, manage_session=True)

def create_app():
    # Enabling config initiation
    app.config.from_object(EnvironmentConfig)
    EnvironmentConfig.init_app(app)

    app.config['SESSION_TYPE'] = 'sqlalchemy'

    bootstrap.init_app(app)
    socketio.init_app(app)

    with app.app_context():
        db.init_app(app)

        from app.models.users import User

        # this code I was previously using but it imports them odd, leaving it because it's cool.
        # Model = declarative_base(name='Model')
        # import_all_subclasses_of(models, Model, locals())
        db.create_all()

    from app.api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    return app


def import_all_subclasses_of(module_to_scan, baseclass, scope):
    """
    :param module_to_scan: Module to scan.
    :param baseclass: A base class to check.
    :param scope: globals(), locals() or a dict-like object.
    """
    path = module_to_scan.__path__
    for mod in pkgutil.iter_modules(path):
        module = mod[0].find_module(mod[1]).load_module(mod[1])

        for name, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, baseclass) and name != baseclass.__name__:
                scope[name] = obj
