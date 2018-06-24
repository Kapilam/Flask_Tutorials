from flask import Flask;
from app import app;


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
                        <h2> header 1 </h2>
                        <h3> header 3</h3> 
                    <body>
              </html>"""
# Server/create
@app.route('/create') # This is the name of the page
def create():
    return "<h2> This is the create page1<h2>"
# server/question<title>
@app.route('/question/<title>')
def question(title):
    return '<h2>' + title + '<h2>';
