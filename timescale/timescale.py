table_name = 'trucks'

import sys
import psycopg2
from psycopg2 import extras
import json
import time
import os
from multiprocessing import Pool
from functools import partial

class TruckObservation(object):
    def __init__(self, j):
        tmp = json.loads(j)

        self.latitude = tmp['latitude']
        self.longitude = tmp['longitude']
        self.speed = tmp['speed']
        self.speed_unit = tmp['speed_unit']
        self.temperature = tmp['temperature']
        self.temperature_unit = tmp['temperature_unit']
        self.EventProcessedUtcTime = tmp['EventProcessedUtcTime']
        self.ConnectionDeviceId = tmp['IoTHub']['ConnectionDeviceId']

    # I know, this is not nice, quick and dirty for the purposes of this blog
    def __getitem__ (self, index):
        if index == 0:
            return self.latitude
        if index == 1:
            return self.longitude
        if index == 2:
            return self.speed
        if index == 3:
            return self.speed_unit
        if index == 4:
            return self.temperature
        if index == 5:
            return self.temperature_unit
        if index == 6:
            return self.EventProcessedUtcTime
        if index == 7:
            return self.ConnectionDeviceId
        else:
            return 0

    def __len__(self):
        return 8

def files_loader(connection_string, table_name, files):
    pool = Pool(processes=5)
    func = partial(pg_load, connection_string, table_name)

    while len(files) > 0:
        print(len(files))
        files_to_load = files[0:5]
        files = files[5::]
        pool.map(func, files_to_load)

def pg_load(connection_string, table_name, file_path):    
    sql = """INSERT INTO trucks(latitude, longitude, speed, speed_unit, temperature, temperature_unit, eventprocessedutctime, connectiondeviceid) 
            VALUES %s"""
    observations = []                        

    conn = psycopg2.connect(connection_string)
    print("Connecting to Database")
    cur = conn.cursor()                
    
    f = open(file_path, "r")
    for x in f:                        
        observations.append(TruckObservation(x))            
        
    print("Execute_values")
    extras.execute_values(cur, sql, observations)
    cur.execute("commit;")

    conn.close()
    print("DB connection closed.")

    del observations[:]

directory_path = sys.argv[1]
connection_string = sys.argv[2]

files = []
for r, d, f in os.walk(directory_path):
    for file in f:
        files.append(os.path.join(r, file))
        
start = time.time()
files_loader(connection_string, table_name, files)
end = time.time()
print("Loaded data into {}".format(table_name))
print("Execution time: {}".format(end - start))