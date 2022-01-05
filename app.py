#set up flask pip install flask, pip install psycopg2-binary
from flask import Flask
app = Flask(__name__)
@app.route('/')
@app.route('/')
def hello_world():
    return 'Hello world'
#in terminal FLASK_APP , export FLASK_APP=app.py , flask run


# Import Python dependencies
import datetime as dt
import numpy as np
import pandas as pd

# Import SQLAlchemy 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# Import Flask 
from flask import Flask, jsonify
# Access the SQLite database
engine = create_engine("sqlite:///hawaii.sqlite")

# database into classes
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create the classes variables
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create a session link from Python to the database
session = Session(engine)
# Use magic method __name__ to check file source of running code
import app
print("example __name__ = %s", __name__)

if __name__ == "__main__":
	print("example is being run directly.")
else:
	print("example is being imported")

# Define Flask app
app = Flask(__name__)
# Define welcome route
@app.route("/")

# Add the routing information for each of the other routes
def welcome():
	return(
	'''
	Welcome to the Climate Analysis API!
	Available Routes:
	/api/v1.0/precipitation
	/api/v1.0/stations
	/api/v1.0/tobs
	/api/v1.0/temp/start/end
	''')
   # Create precipitation route
@app.route("/api/v1.0/precipitation")

# Create the precipitation() function
def precipitation():
	# Calculate the date one year ago from the most recent date
	prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

	# Query: get date and precipitation for prev_year
	precipitation = session.query(Measurement.date,Measurement.prcp) .\
		filter(Measurement.date >= prev_year).all()
		
	# Create dictionary w/ jsonify()--format results into .JSON
	precip = {date: prcp for date, prcp in precipitation}
	return jsonify(precip)
@app.route("/api/v1.0/stations")

def stations():
	results = session.query(Station.station).all()
	# Unravel results into one-dimensional array:
		# `function np.ravel()`, `parameter = results`
	# Convert results array into a list with `list()`
	stations = list(np.ravel(results))
	return jsonify(stations=stations) 
@app.route("/api/v1.0/tobs")

def temp_monthly():
	prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
	results = session.query(Measurement.tobs).\
		filter(Measurement.station == 'USC00519281').\
		filter(Measurement.date >= prev_year).all()
	temps = list(np.ravel(results))
	return jsonify(temps=temps)
# Provide both start/end date routes:
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Add parameters to `stats()`: `start` and `end` parameters
def stats(start=None, end=None):
	# Query: min, avg, max temps; create list called `sel`
	sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

	# Add `if-not` statement to determine start/end date
	if not end:
		results = session.query(*sel).\
			filter(Measurement.date >= start).\
			filter(Measurement.date <= end).all()
		temps = list(np.ravel(results))
	return jsonify(temps=temps)

		# NOTE: (*sel) - asterik indicates multiple results from query: minimum, average, and maximum temperatures

	# Query: Calc stats
	results = session.query(*sel).\
		filter(Measurement.date >= start).\
		filter(Measurement.date <= end).all()
	temps = list(np.ravel(results))
	return jsonify(temps=temps)

#* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
#127.0.0.1 - - [30/Dec/2021 14:07:06] "GET / HTTP/1.1" 200 -
#/usr/local/bin/python3.9 /Users/tanyaczeban/Desktop/class/surfs_up/app.py
#127.0.0.1 - - [30/Dec/2021 14:13:49] "GET / HTTP/1.1" 200 -
