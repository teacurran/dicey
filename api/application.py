"""This file is the main module which contains the app, where all the good
stuff happens. You will always want to point your applications like Gunicorn
to this file, which will pick up the app to run their servers.
"""
from app import create_app, socketio
from decouple import config

app = create_app()
# migrate = Migrate(app, db)

if __name__ == '__main__':
    socketio.run()


