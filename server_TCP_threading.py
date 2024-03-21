import socket
import threading  # Import thư viện threading để sử dụng luồng

serverName = "127.0.0.1"   # Địa chỉ IP của server
serverPort = 12000          # Cổng mà server đang lắng nghe

# Tạo socket của server
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liên kết socket với địa chỉ IP và cổng
serverSocket.bind((serverName, serverPort))

def handle_client(connectionSocket, clientAddress):
    try:
        while True:
            message = connectionSocket.recv(2048)  # Nhận dữ liệu từ client 
            if not message:  # Kiểm tra nếu client đã đóng kết nối
                break
            print(message)  # In ra dữ liệu nhận được từ client nếu khác rỗng
            modifiedMessage = message.upper()  # Chuyển đổi dữ liệu nhận được thành chữ hoa
            connectionSocket.send(modifiedMessage)  # Gửi dữ liệu đã được chuyển đổi về lại cho client
    except KeyboardInterrupt:  # Bắt ngoại lệ :nhấn Ctrl+C để ngắt kết nối.
        print("\nNgắt kết nối.")
    finally:
        connectionSocket.close()  # Đóng kết nối với client khi kết thúc xử lý

print("The server is ready to receive:")
serverSocket.listen(3)  # Server bắt đầu lắng nghe các kết nối từ client, với số lượng kết nối tối đa là 3

try:
    while True:
        connectionSocket, clientAddress = serverSocket.accept() 
        # Chấp nhận kết nối từ client và tạo một luồng riêng biệt để xử lý client đó
        client_thread = threading.Thread(target=handle_client, args=(connectionSocket, clientAddress))
        client_thread.start()  # Khởi động luồng để xử lý client
finally:
    serverSocket.close()  # Đóng socket của server khi thoát chương trình
