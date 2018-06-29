"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
# DO NOT TOUCH-We need this code for evry project
# import flask
from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

# END DO NOT TOUCH

#Project specific code goes here...

# import all of route codes from route.py
from routes import * #import all routes. * mean all"
# To Launch the server
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
