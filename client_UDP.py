import socket

serverName="127.0.0.1"
serverPort=12000

clientSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Tạo socket của client, clientSocket. 
# -Tham số đầu tiên cho biết kiểu địa chỉ IP, cụ thể AF_INET chỉ ra mạng đang sử dụng IPv4. 
# - Tham số thứ 2 cho biết loại socket là UDP.

message=input('Input Lowercase sentence: ')

clientSocket.sendto(message.encode(),(serverName,serverPort))
# Phương thức sendto() đính kèm địa chỉ đích (serverName, serverPort) vào message và gửi 
# gói kết quả vào socket của process, clientSocket.

modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
#- khi một gói từ Internet đến socket của client, dữ liệu của gói được đưa vào biến modifiedMessage và 
# địa chỉ nguồn của gói được đưa vào biến serverAddress
#- Phương thức recvfrom lấy kích thước bộ đệm 2048 làm đầu vào.

print(modifiedMessage.decode())

clientSocket.close()