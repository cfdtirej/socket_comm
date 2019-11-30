"""
list_dict_client.pyが送ってきたデータを受け取る
"""
import socket, datetime

rhost = "" # receive info
port = 5678
size = 4096

"""クライアントからデータを受け取る"""
rserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rserver.bind((rhost,port))
rserver.listen()
print("接続待ち")

while True:
    client, addr = rserver.accept()
    time = datetime.datetime.now()
    msg = "繋がったよ〜"
    print(time, msg)
    print(client)

    try:
        while True:
            data = client.recv(size)
            if data:
                print((data.decode("utf-8")))
            elif not data:
                break
    except:
        # client.close()
        print(data.decode("utf-8"))
        

