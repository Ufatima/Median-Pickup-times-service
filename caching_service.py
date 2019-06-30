"""data reading and caching"""
import pickle
import pandas as pd

FILENAME = 'pickup_times.csv'


class LoadData(object):
    """this class is used to read data from csv, and load data to redis"""
    def data_caching(redis_con):
        """ this function used for caching using redis"""
        data_frame = pd.read_csv(FILENAME)
        for index, row in data_frame.iterrows():
            pickled = pickle.dumps(row)
            key = str(index) + ":" + str(row['location_id'])
            redis_con.setnx(key, pickled)
        return redis_con
