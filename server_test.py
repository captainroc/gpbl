# Python代码可做聊天室的服务器端部分。
import _thread
import socket
import threading
"""AF_INET is the address domain of the 
socket. This is used when we have an Internet Domain with 
any two hosts The 2nd context of the code is the type of socket. """
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# piece of code to allow IP address & Port
host="0.0.0.0"
port=6688
s.bind((host,port))
s.listen(5)
clients=[]
#code to allow users to send messages
def connectNewClient(c):
     while True:
        global clients
        msg = c.recv(2048)
        msg ='Online ('+str(clients.index(c)+1)+'):  '+msg.decode('UTF-8')
        sendToAll(msg,c)
def sendToAll(msg,con):
    for client in clients:
        client.send(msg.encode('UTF-8')) 
       
while True:
    try:    
        c,ad=s.accept()
        # Display message when user connects
        print('start ')
        clients.append(c)
        c.send(('Online ('+str(clients.index(c)+1)+')').encode('UTF-8'))
        _thread.start_new_thread(connectNewClient,(c,))
    except:
        c.close()

