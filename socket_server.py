
import socket
import time
phone_clients =[]
clients = []  # 儲存用戶端socket物件的列表變數
HOST = '0.0.0.0'
PORT = 5438
s = socket.socket()
s.bind((HOST, PORT))
s.setblocking(False)  # 將此socket設成非阻塞
s.listen(5)
print('{}伺服器在{}埠開通了！'.format(HOST, PORT))

	
while True:
    try:
        client, addr = s.accept()
        print('用戶端位址：{}，埠號：{}'.format(addr[0], addr[1]))
        # 也把跟用戶端連線的socket設成「非阻塞」
        client.setblocking(False) 
        # 將此用戶端socket物件存入clients列表備用
        clients.append(client)
    except:
        pass  # 不理會錯誤
 
    # 逐一處理clients列表裡的每個用戶端socket…
    for client in clients:
        try:
            msg = client.recv(1024).decode('utf8')

            print('收到訊息：' + msg)
            reply = ''
 
            if  'phone' in msg:
                phone_clients.append(client)
                reply = b'Hello Phone!'
            elif 'quit' in msg or len(msg)==0:

                client.send(b'Bye')
                client.close()
                # 將此用戶端socket從列表中移除
                clients.remove(client)
                break  # 退出for迴圈
            else:
                reply = b'what??'

            client.send(msg.encode('UTF-8'))
            for client in phone_clients:
                client.send(msg.encode('UTF-8'))           
        except:
            pass  # 不理會錯誤