#import flask 
from flask import Flask
#create new flask instance- __x__=magic method
app = Flask(__name__)
#add route/starting pnt/=want to put root in routes=highes heir
@app.route('/')
def hello_world():
    return 'Hello world'