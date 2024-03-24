# Import thư viện Shodan và os
import shodan
import os

# Khởi tạo một danh sách để lưu trữ các địa chỉ IP của máy chủ FTP Anonymous
servers = []

# Lấy khóa API Shodan từ biến môi trường
SHODAN_API_KEY = os.environ.get('SHODAN_API_KEY')

try:
    # Khởi tạo đối tượng Shodan với khóa API đã cung cấp
    shodan_api = shodan.Shodan(SHODAN_API_KEY)
    
    # Tìm kiếm các máy chủ FTP với cổng 21 và người dùng đăng nhập ở chế độ Anonymous
    # Sử dụng cursor để lấy kết quả từng trang
    cursor = shodan_api.search_cursor('port:21 Anonymous user logged in')
    
    # Đếm số lượng máy chủ được tìm thấy
    num_hosts = 0
    
    # Lặp qua từng kết quả và thêm địa chỉ IP của máy chủ vào danh sách
    for result in cursor:
        if 'ip_str' in result:
            servers.append(result['ip_str'])
            num_hosts += 1

    # In ra số lượng máy chủ được tìm thấy
    print('Number of hosts:', num_hosts)
    
    # In ra từng địa chỉ IP của máy chủ
    for server in servers:
        print(server)
        
# Bắt các ngoại lệ nếu có lỗi xảy ra trong quá trình thực thi
except Exception as e:
    print('Error:', e)
