from flask import Flask, url_for;
from app import app;


# server/
@app.route('/')
def hello():
    """Renders a sample page."""
    createLink = "<a href='" + url_for('create') + "'>Create a question</a>";
    return """<html>
                    <head>
                        <title> Hello, world </title>
                     </head>
                     <body>
                            """ + createLink + """
                        <h1> Hello World KM </h1>
                        <h2> type "/question/km in url" </h2>
                        <h3> you will see km page</h3> 
                    <body>
              </html>"""
# Server/create
@app.route('/create') # This is the name of the page
def create():
    return "<h2> This is the create page1<h2>"
# server/question<title>
@app.route('/question/<title>')
def question(title):
    return '<h2>' + title + '</h2>';
