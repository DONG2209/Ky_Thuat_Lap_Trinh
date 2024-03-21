import socket 

ip='42.112.213.88'   #Địa chỉ IP của máy chủ cần kiểm tra.
portList=[21,22,23,80,443]  #Danh sách các cổng muốn kiểm tra.

for port in portList:
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Tạo một đối tượng socket để thực hiện kết nối TCP.
    resultt=sock.connect_ex((ip,port))   #Thử kết nối đến cổng port trên địa chỉ IP . 
    #Phương thức connect_ex() trả về mã lỗi nếu kết nối không thành công, ngược lại trả về 0.
    print(port,":",resultt)  #In ra kết quả của kết nối cho mỗi cổng.
    sock.close()   #Đóng kết nối TCP sau khi kiểm tra xong mỗi cổng.