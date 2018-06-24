"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

# import flask
from flask import Flask
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


# server/
@app.route('/')
def hello():
    """Renders a sample page."""
    return """<html>
                    <head>
                        <title> Hello, world </title>
                     </head>
                     <body>
                        <h1> Hello World KM </h1>
                        <h2> header 1 <h2>
                    <body>
              </html>"""

# To Launch the server
if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
