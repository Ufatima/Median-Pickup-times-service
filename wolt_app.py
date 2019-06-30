""" this module creates a rest api service that returns a median time
for a given location between specific time """

import pickle
from statistics import median_low
from flask import Flask, request
from flask_restful import Api, Resource
import dateutil.parser
import redis as rd
from caching_service import LoadData as Redis_data

REDIS_CONN = rd.Redis(host='127.0.0.1', port=6379, db=0)
rds = Redis_data.data_caching(REDIS_CONN)

APP = Flask(__name__)
API = Api(APP)


class MedianPickupTime(Resource):
    """ this class """

    def __init__(self):
        pass

    def get(self):

        """ this method used for GET Request
        return the median value"""

        location_id = request.args.get('location_id')
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')

        start_time = dateutil.parser.parse(start_time)
        end_time = dateutil.parser.parse(end_time)

        median_value = self.median_calculation(location_id, start_time, end_time)
        median = {
            "median": median_value
        }
        return median

    def median_calculation(self, location_id, start_time, end_time):
        """ calculate median value"""

        pickup_time_list = []

        # building the key search pattern for redis
        build_key = '*:' + str(location_id)
        keys = rds.keys(build_key)

        for row in keys:
            entry = pickle.loads(rds.get(row))
            loc_val = int(entry['location_id'])
            location_id = int(location_id)

            if location_id == loc_val:
                iso_time = entry['iso_8601_timestamp']
                iso_time = iso_time[:-1]
                iso_time_parsed = dateutil.parser.parse(iso_time)

                if start_time <= iso_time_parsed <= end_time:
                    pickup_time_list.append(entry['pickup_time'])

        pickup_time_list_length = len(pickup_time_list)
        if pickup_time_list_length > 0:
            median_value = median_low(pickup_time_list)
        else:
            median_value = None
        return median_value


API.add_resource(MedianPickupTime, "/median_pickup_time")
APP.run(debug=True)
