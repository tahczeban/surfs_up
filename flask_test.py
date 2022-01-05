#Import Flask
from flask import Flask

#Create a new Flask instance called "app"
app = Flask(__name__)

#Creat a Flask route
##Define the starting point aka the "root"
@app.route('/')
def hello_world():
   return 'Hello World'

#HOW TO RUN FLASK VIA TERMINAL
# 1. Go to Terminal, and enter 'export FLASK_APP=flask_test.py'
# 2. Then  ****** not how mod said for mac but 'set FLASK_APP=app.py'
# 3. Then  'flask run'
#  Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)