import socket  #Khai báo module

serverName="127.0.0.1"   #địa chỉ ip server
serverPort=12000        # Cổng mà server đang lắng nghe

serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Tạo socket của server, serverSocket. 
# -Tham số đầu tiên cho biết kiểu địa chỉ IP, cụ thể AF_INET chỉ ra mạng đang sử dụng IPv4. 
# - Tham số thứ 2 cho biết loại socket là TCP.
serverSocket.bind((serverName,serverPort))  #Dùng để lắng nghe đến địa chỉ ip và cổng

print("the server is ready to receive:")
serverSocket.listen(3)    # Server bắt đầu lắng nghe các kết nối từ client, với số lượng kết nối tối đa tại 1 thời điểm là 3
try:
    while True:
        # Chấp nhận kết nối từ client và trả về một đối tượng socket mới (connectionSocket) và địa chỉ của client (clientAddress)
        connectionSocket, clientAddress = serverSocket.accept() 
        try:
            while True:
                message=connectionSocket.recv(2048)  # Nhận dữ liệu từ client 
                if not message:  # Kiểm tra nếu client đã đóng kết nối ,thoát khỏi vòng lặp
                    break
                print(message)  # In ra dữ liệu nhận được từ client nếu khác rỗng
                modifiedMessage=message.upper() # Chuyển đổi dữ liệu nhận được thành chữ hoa
                connectionSocket.send(modifiedMessage)  # Gửi dữ liệu đã được chuyển đổi về lại cho client sử dụng địa chỉ của client

        except KeyboardInterrupt:  # Bắt ngoại lệ :nhấn Ctrl+C để ngắt kết nối.
            print("\nNgắt kết nối.")
            break
finally:
    serverSocket.close()  # Đóng socket của server khi thoát chương trình