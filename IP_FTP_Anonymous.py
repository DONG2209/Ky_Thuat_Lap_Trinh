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
    results = shodan_api.search('port:21 Anonymous user logged in')
    
    # In ra số lượng máy chủ được tìm thấy
    print('Number of hosts:', len(results['matches']))
    
    # Lặp qua các kết quả và thêm địa chỉ IP của máy chủ vào danh sách
    for result in results['matches']:
        if result['ip_str'] is not None:   # nêu ip không rỗng thì thêm vào mảng servers
            servers.append(result['ip_str'])

    # In ra từng địa chỉ IP của máy chủ
    for server in servers:
        print(server)
        
# Bắt các ngoại lệ nếu có lỗi xảy ra trong quá trình thực thi
except Exception as e:
    print('Error:', e)
