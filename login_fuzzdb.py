# Import thư viện requests để gửi HTTP requests
import requests

# Mở file 'logins.txt' trong chế độ đọc ('r') và gán nó cho biến filehandle
with open('logins.txt', 'r') as filehandle:
    # Đọc từng dòng trong file và loại bỏ các ký tự trống ở đầu và cuối mỗi dòng
    # Lưu các dòng vào list logins
    logins = [line.strip() for line in filehandle]

# Khai báo biến domain để lưu địa chỉ của trang web sẽ kiểm tra
domain = "http://testphp.vulnweb.com"

# Duyệt qua từng phần tử trong list logins
for login in logins:
    # In ra thông điệp kiểm tra và địa chỉ URL được sử dụng để kiểm tra, kết hợp domain và login
    print("Checking...", domain + login)
    
    # Gửi một HTTP GET request đến địa chỉ URL được kết hợp từ domain và login
    # Lưu response vào biến response
    response = requests.get(domain + login)
    
    # Kiểm tra xem response có mã status là 200 không, tức là request thành công
    if response.status_code == 200:
        # Nếu request thành công, in ra thông điệp thông báo rằng tài nguyên đăng nhập đã được phát hiện
        print("Login resource detected:", login)
