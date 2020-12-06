import datetime as dt
import numpy as np
import pandas as pd 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.Measurement
Station = Base.classes.station

session = Session(engine)

#### Flask Setup
app = Flask(__name__)


###Flask Routes
@app.route("/")
def Welcome():
    """List of all available api routes."""
    return(
        f"Available routes below:<br/>"
        f"<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"/api/v1.0/tobs<br/>"
        f"<br/>"
        f"/api/v1.0/<start><br/>"
        f"<br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    """Query for the dates and temperature observations from the last year."""

    results = session.query(Measurement.date, Measurement.prcp).\
                            filter(Measurement.date <= End_date).\
                            filter(Measurement.date >= Start_date).all()

    list = []
    for result in results:
        dict = {"Date": result[0], "Precipitation": result[1]}
        list.append(dict)
    
    return jsonify(list)


@app.route("/api/v1.0/stations")
def stations()

    """Return a JSON list of stations from the dataset in the form of dictionary."""

    stations = session.query(Station.station, Station.name).all()
                            
    list = []
    for station in stations:
        dict = {"Station ID": stations[0], "Station Name": stations[1]}
        list.append

    return jsonify(list)


@app.route("/api/v1.0/tobs")
def tobs():
    """ Return a JSON list of Temperature Observations (tobs) for the previous year."""  
    
    tobs = session.query(Measurement.date,Measurement.tobs).\
                            filter(Measurement.date <= End_date).
                            filter(Measurement.date >= Start_date).all()
    list = []
    for temp in tobs:
        dict = {"date": temp[0], "tobs": temp[1]}
        list.append(dict)

    return jsonify(list)

    