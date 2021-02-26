from time import sleep
import serial
from msvcrt import getch
import socket
##==============================================================================



ser =serial.Serial("COM4", 115200, timeout=2) # Establish the connection on a specific port
##==============================================================================

##=======getchar========================
# def getchar():
#     #Returns a single character from standard input
#     key = getch()                    ##Get byte         ex: b'a'
#     key_num=ord(key)           ##convert byte to integer    97
#     key_chr=chr(key_num)    ##convert integer to char       'a'
#     return key_num
##====================================

##======Write Serial Command to arduino============
def SerialWrite(cmd):
    ser.write(cmd)
    rv=ser.readline()
    #print (rv) # Read the newest output from the Arduino
    print (rv.decode("utf-8")) 

    ser.flushInput()
##====================================

##=======Get  Ready================
print("Connecting to Arduino.....")
for i in range (1,10):
    rv=ser.readline()
    print("Loading...")
    #Debug print (rv) # Read the newest output from the Arduino
    print (rv.decode("utf-8")) 
    ser.flushInput()
    sleep(1) # Delay for one tenth of a secon
    Str=rv.decode("utf-8")
    #Debug print(Str[0:5])
    if Str[0:5]=="Ready":  
          print("Get Arduino Ready !")
          break
##------------------------------------------------------
  



# 建立一個socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 主動去連線本機IP和埠號為6688的程序，localhost等效於127.0.0.1，也就是去連線本機埠為6688的程序
client.connect(('127.0.0.1',5438))
client.sendall(b'phone')
    # 接受控制檯的輸入





##===Get char from keyboard then send to arduino and get it back to print in screen==
try:
    while True:

            # 接受客户端的数据

        # 接收服務端的反饋資料
        rec_data = client.recv(1024)

        # 如果接受到客户端要quit就结束循环
    #     if data == b'quit' or data == b'':
    #         print(b'the client has quit.')
    #         break
    #     else:
            # 发送数据给客户端

            
        
        print('ready to control!')
        print(b'the client say:' + rec_data)
        SerialWrite(rec_data)
#         if a==4:
#             break
    #     if data==27:  ##ESC
    #          break
#     ser.close()    
#     server.close()

except:
    pass

