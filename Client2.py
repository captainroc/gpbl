import socket
import serial  # 引用pySerial模組

COM_PORT = 'COM5'    # 指定通訊埠名稱
BAUD_RATES = 9600    # 設定傳輸速率
ser = serial.Serial(COM_PORT, BAUD_RATES)   # 初始化序列通訊埠

# 创建一个socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 主动去连接局域网内IP为192.168.27.238，端口为6688的进程
client.connect(('172.16.1.114', 6688))

while True:
    # 接受控制台的输入
    #data = input()
    data_raw = ser.readline()  # 讀取一行
    data = data_raw.decode()   # 用預設的UTF-8解碼
    print('接收到的原始資料：', data_raw)
    print('接收到的資料：', data)
    # 对数据进行编码格式转换，不然报错
    #data = data.encode('utf-8')
    # 如果输入quit则退出连接
#     if data == b'quit':
#         print(b'connect quit.')
#         break
#     else:
        # 发送数据
    client.sendall(data)
        # 接收服务端的反馈数据
    rec_data = client.recv(1024)
    print(b'form server receive:' + rec_data)

# 发送数据告诉服务器退出连接
client.sendall(b'quit')
client.close()