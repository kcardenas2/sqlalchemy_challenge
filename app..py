import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
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
session = Session(engine)

# # flask
# app = Flask(__name__)

# hello_dict = {"Hello": "World!"}

# # flask routes
# @app.route("/")
# def home():
#     return (f""
#     f"/api/v1.0/precipitation"
#     f"/api/v1.0/stations"
#     f"/api/v1.0/tobs"
#     f"/api/v1.0/<start>"
#     f"/api/v1.0/<start>/<end>")


# @app.route("/api/v1.0/precipitation")
# def precipatation():
#     results=(session.query(Measurement.date, Measurement.prcp)
#                     .filter(Measurement.date> year_ago).\
#                     order_by(Measurement.date).all())

#     precip_scores=[]
#     for results in results:
#             precip_scores_dict={}
#             precip_scores_dict["date"]=result.date
#             precip_scores_dict["prcp"]=result.prcp
#             precip_scores.append(precip_scores_dict)

#     return jsonify(precip_scores)


# @app.route("/api/v1.0/stations")
# def stations():
#     results= session.query(Station.station).all()
    
#     Stations=[]
#     for Stations in stations:
#         station_dict={}
#         Stations.append(station_dict)

#     return jsonify(Stations)

# @app.route("/api/v1.0/tobs")
# def tobs():
#     results= ()

# @app.route("/api/v1.0/<start>")
# def start():
#     results=session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
# active_stations

#     observations=[]
#     for min,avg,max in results:
#         start_dict={}
#         start_dict["Min"]=min
#         start_dict["Average"]=avg
#         start_dict["Max"]=max
#         observations.append(start_dict)

#     return jsonify(observations)

# @app.route("/api/v1.0/<start>/<end>")
# def first_last():
#     results=session.query(Measurement.station, Measurement.date, Measurement.tobs).filter(Measurement.date>="2016-08-24").filter(Measurement.date<="2017-08-23").filter(Measurement.station=="USC00519281").all()


# Both=[]
# for min,avg,max in results:
#     first_last_dict={}
#     first_last_dict["Min"]=min
#     first_last_dict["Average"]=avg
#     first_last_dict["Max"]=max
#     Both.append(start_dict)

# return jsonify(Both)


# if __name__ == "__main__":
#     app.run(debug=True)


# In[ ]:




