import socket

serverPort=12000

serverSocket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("the server is ready to receive:")

while True:
    message,clientAddress=serverSocket.recvfrom(2048)
    print(message)
    modifiedMessage=message.upper()
    serverSocket.sendto(modifiedMessage,clientAddress)

# vòng lặp while sẽ cho phép UDPServer nhận và xử lý các gói từ máy khách vô thời hạn
