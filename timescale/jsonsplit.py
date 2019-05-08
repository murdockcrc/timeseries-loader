table_name = 'trucks'

import sys
import psycopg2
from psycopg2 import extras
import json
import time

def split_file(file_path, size):    
    try:
        with open(file_path) as f:
            i = 0
            file_counter = 0      
            file_name = "split." + file_path + str(file_counter)
            new_file = open(file_name, "w+")

            for line in f:                
                new_file.write(line)                                    
                i += 1
                if i >= size:
                    new_file.close() 
                    file_counter += 1                    
                    i = 0
                    file_name = "split." + file_path + str(file_counter)
                    new_file = open(file_name, "w+")    

    except Exception as e:
        print('Error {}'.format(str(e)))

file_path = sys.argv[1]
split_size = int(sys.argv[2])
split_file(file_path, split_size)