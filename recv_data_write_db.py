#Receive data from client and Write receive data to InfluxDB

import csv
import datetime
import json
import os
import socket
import sys
import time

from influxdb import InfluxDBClient

# load recv_data_write_db.json
conf_dir_path = os.path.normpath('%s/../conf_dir' %__file__)
json_conf_path = os.path.join(conf_dir_path, "config.json")
print(json_conf_path)
f = open(json_conf_path, "r", encoding="UTF-8")
conf_file = json.load(f)

# receive info
recv_host = conf_file["socket"]["host"]
recv_port = conf_file["socket"]["port"]
buffer_size = conf_file["socket"]["size"]

#InfluxDB info
db_client = InfluxDBClient(
    host = conf_file["InfluxDB"]["host"], 
    port = conf_file["InfluxDB"]["port"],
    username = conf_file["InfluxDB"]["username"], 
    password = conf_file["InfluxDB"]["password"], 
    database = conf_file["InfluxDB"]["database"]
    )


def write_db():
""" def function for receive data from client and write data to InfluxDB """
    try:
        recv_srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        recv_srv.bind((recv_host,recv_port))
        recv_srv.listen()
        print("Wating for connect", datetime.datetime.now())
        client, addr = recv_srv.accept()

        start_datetime = datetime.datetime.now()
        print("Connected", start_datetime)
        start_time = time.time()
        amass_data = b""
        while True:
            data = client.recv(buffer_size)
            amass_data += data
            if not data:
                # decode unicode-escape & Line feed / split
                decode_data = amass_data.decode("unicode-escape").splitlines()
                # Write receive data to InfluxDB
                for i in decode_data:
                    write_array = [eval(i)] # str→dict
                    # db_client.write_points(write_array)
                fin_time = time.time() - start_time
                fin_datetime = datetime.datetime.now()
                print(client, "\n", datetime.datetime.now(), "-----NOT DATA-----")
                break
    except:
        print("Error")
    print("End Time : ", fin_time , "[sec]")
    with open("./socket_comm/fin_time.csv", "a", newline="") as f:
        writer = csv.writer(f, lineterminator="\n")
        writer.writerow([start_datetime, fin_datetime, fin_time])        
    client.close()
    sys.exit()


write_db()

