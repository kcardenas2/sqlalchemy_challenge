import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base, name_for_collection_relationship
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

# import flask
from flask import Flask, jsonify

# create connection
engine= create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect= True)

# Save references to each table
Measurement= Base.classes.measurement
Station= Base.classes.station

# Create our session 
# session = Session(engine)

# flask
app = Flask(__name__)


# flask routes
@app.route("/")
def home():
    return (f""
    f"/api/v1.0/precipitation"
    f"/api/v1.0/stations"
    f"/api/v1.0/tobs"
    f"/api/v1.0/<start>"
    f"/api/v1.0/<start>/<end>")


@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    year_ago= dt.date(2017,8,23)-dt.timedelta(days=365)
    session.close()
    results=(session.query(Measurement.date, Measurement.prcp)
                    .filter(Measurement.date> year_ago).\
                    order_by(Measurement.date).all())

    precip_scores=[]
    for results in results:
            precip_scores_dict={}
            precip_scores_dict["date"]=results.date
            precip_scores_dict["prcp"]=results.prcp
            precip_scores.append(precip_scores_dict)

    return jsonify(precip_scores)


@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    station_data= [Station.station, Station.name]
    results= session.query(*station_data).all()
    session.close()
    stations=[]
    for station,name in results:
        station_dict={}
        station_dict["name"]= name
        station_dict["stations"]= station
        stations.append(station_dict)

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    recent_date= session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    year_ago= dt.date(2017,8,23)-dt.timedelta(days=365)
    years_ago=[Measurement.date, Measurement.tobs]
    results= session.query(*years_ago).filter(Measurement.date >= years_ago).all()
    session.close()
    tobs=[]
    for date, tobs in results:
        tobs_dict={}
        tobs_dict["Date"] = date
        tobs_dict["Temp observations"]= tobs
        tobs.append(tobs_dict)
    return(tobs)


@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)
    results=session.query(func.min(Measurement.tobs),
             func.max(Measurement.tobs),
             func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    session.close()
    observations=[]
    for min,avg,max in results:
        start_dict={}
        start_dict["Min"]=min
        start_dict["Average"]=avg
        start_dict["Max"]=max
        observations.append(start_dict)

    return jsonify(observations)

@app.route("/api/v1.0/<start>/<end>")
def first_last(start, end):
    session = Session(engine)
    results=session.query(func.min(Measurement.tobs),
             func.max(Measurement.tobs),
             func.avg(Measurement.tobs)).\
                 filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()

    Both=[]
    for min,avg,max in results: 
        start_end_dict={}
        start_end_dict["Min"]=min
        start_end_dict["Average"]=avg
        start_end_dict["Max"]=max
        Both.append(start_end_dict)

    return jsonify(Both)


if __name__ == "__main__":
    app.run(debug=True)





