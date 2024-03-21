import socket  #Khai báo module

# Địa chỉ IP và cổng của server
ServerName="127.0.0.1"    # Đây là địa chỉ loopback, tức là cùng máy
ServerPort=12000        # Cổng mà server đang lắng nghe

ClientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Tạo socket của client, clientSocket. 
# -Tham số đầu tiên cho biết kiểu địa chỉ IP, cụ thể AF_INET chỉ ra mạng đang sử dụng IPv4. 
# - Tham số thứ 2 cho biết loại socket là TCP.

ClientSocket.connect((ServerName, ServerPort))  # Kết nối đến server

try:
    while True:
        message=input('Input Lowercase sentence: ')
        #người dùng sử dụng bàn phím để nhập dữ liệu, dữ liệu này được đưa vào biến message
        
        ClientSocket.send(message.encode())
        # Phương thức send() gửi message tới server đã kết nối 
        
        modifiedMessage=ClientSocket.recv(2048)
        #- khi một gói từ Internet đến socket của client, dữ liệu của gói được đưa vào biến modifiedMessage 
        #- Phương thức recv lấy kích thước bộ đệm 2048 làm đầu vào.

        print(modifiedMessage.decode()) #Xuất ra màn hình từ sẻver trả về

except KeyboardInterrupt:   # Bắt ngoại lệ khi người dùng nhấn Ctrl+C để ngắt kết nối.
    print("\nNgắt kết nối.")
    ClientSocket.close()   # Đóng kết nối với server khi thoát chương trình

