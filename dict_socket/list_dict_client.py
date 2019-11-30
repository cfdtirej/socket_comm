"""
list_dict_server.pyにデータ転送
ディクショナリ形式のデータをループで回してサーバーに転送する
"""
import socket
import json
import time
import datetime

host = ""
port = 5678
size = 4096
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
for i in range(5):
    # t = 10
    t = str(datetime.datetime.now())
    a = {"data": i, "time": t},{"a":i,"b":"難しいよー"}
    b = json.dumps(a).encode("utf-8")
    c = ",".encode("utf-8")

    client.send(b)
client.close()
