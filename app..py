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
    data=[Measurement.date, Measurement.tobs]
    results= session.query(*data).filter(Measurement.date >= date).all()
    session.close()
    tobs=[]
    for date, tobs in result:
        tob_dict={}
        tob_dict["Date"] = date
        tob_dict["Temp observations"]= tobs
        tobs.append(tob_dict)
    return(tobs)


@app.route("/api/v1.0/<start>")
def start():
    session = Session(engine)
    results=session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
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
def first_last():
    session = Session(engine)
    results=session.query(Measurement.station, Measurement.date, Measurement.tobs).filter(Measurement.date>="2016-08-24").filter(Measurement.date<="2017-08-23").filter(Measurement.station=="USC00519281").all()
    session.close()

    Both=[]
    for min,avg,max in results: 
        first_last_dict={}
        first_last_dict["Min"]=min
        first_last_dict["Average"]=avg
        first_last_dict["Max"]=max
        Both.append(start_dict)

    return jsonify(Both)


if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




