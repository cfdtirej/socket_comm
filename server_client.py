""" 
クライアントからデータを受け取る.
受け取ったデータを別サーバーに送る.
"""
import socket, datetime

# receive info
rhost = "localhost"
shost = "192.168.30.145"
port = 5678
size = 4096

"""このコンピュータのソケット"""
rserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
rserver.bind((rhost,port))
rserver.listen()


while True:
    client, addr = rserver.accept()
    time = datetime.datetime.now()
    msg = "繋がった〜"
    print(time, msg)
    print(client)

    try:
        while True:
            data = client.recv(size)
            if not data:
                break
            print(data.decode("utf-8"))
    except:
        print("Error|多分,クライアント側がクローズした")
    client.sendall(msg.encode("utf-8"))
    client.close()

    """別サーバーにデータを送る"""
    sclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sclient.connect((shost, port))
    sclient.sendall(data)
    sclient.close()

