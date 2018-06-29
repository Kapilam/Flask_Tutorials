from flask import Flask, url_for, request, render_template;
from app import app;
import redis;

#Connect to redis data store in Azure clouse
#r = redis.StrictRedis(host='kmredisdns.redis.cache.windows.net', port=6380, db=0, password=AvfpG+2Uc8aJ7AADoVdS7uHzXaSeyIxjwPDZIdt66CM=ssl=True, charset="utf-8", decode_responses=True);

#Connect to local host
r = redis.StrictRedis(host='localhost', port=6379, db=0, , charset="utf-8", decode_responses=True);


# server/
@app.route('/')
def hello():


#alternative ways to connect to redis, each commnad is equivalent.
#r=credits.StrictRedis(); 
#r=credits.StrictRedis('localhost,6379, 0);
 

    createLink = "<a href='" + url_for('create') + "'>Create a question</a>";
    return """<html>
                   <head>
                       <title>Hello, world!</title>
                    </head>
                    <body>
                       """ + createLink + """
                    </body>
               </html>""";

# define a function to create a new question
# server/create
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        # send the user the form
        return render_template('CreateQuestion.html');
    elif request.method == 'POST':
        # read form data and save it
        title = request.form['title'];
        question = request.form['question'];
        answer = request.form['answer'];

        # Store data in Redis data store
        # Key name will be whatever title they typed in : Question 
        # e.g. music:question countries:question
        # e.g. music:answer countries:answer


        # Code to store data in Radis
        r.set(title +':question', question)
        r.set(title +':answer',answer)
    
        return render_template('CreatedQuestion.html', question = question);
    else:
        return "<h2>Invalid request</h2>";


# Define a function to obtain questions under one titile 
# server/question/<title>
@app.route('/question/<title>', methods=['GET', 'POST'])
def question(title):
    if request.method == 'GET':
        
        # send the user the form
        question = r.get(title+':question')
        # Read question from data store
      
        return render_template('AnswerQuestion.html', question = question);
    elif request.method == 'POST':
        # User has attempted answer. Check if they're correct
        submittedAnswer = request.form['submittedAnswer'];

        # Read answer from data store
        # Susan - please add code here
        answer = r.get(title+':answer')

        if submittedAnswer == answer:
            return "Correct!"
            #return render_template('Correct.html');
        else:
            return render_template('Incorrect.html', submittedAnswer = submittedAnswer, answer = answer);
    else:
        return '<h2>Invalid request</h2>';