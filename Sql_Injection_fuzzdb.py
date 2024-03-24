import requests

# Địa chỉ URL của trang web cần kiểm tra, chứa tham số dùng để truy vấn CSDL (cat)
domain = "http://testphp.vulnweb.com/listproducts.php?cat="

# Danh sách các chuỗi tấn công SQL Injection từ FuzzDB
mysql_attacks = []

# Mở file chứa danh sách các chuỗi tấn công SQL Injection và lưu vào mysql_attacks
with open('MySQL.txt', 'r') as filehandle:
    mysql_attacks = [line.strip() for line in filehandle]  # Đọc từng dòng trong file và loại bỏ các ký tự trống ở đầu và cuối mỗi dòng

# Duyệt qua từng chuỗi tấn công trong mysql_attacks
for attack in mysql_attacks:
    # Gửi HTTP GET request đến trang web với tham số cat được thay đổi bằng chuỗi tấn công hiện tại
    response = requests.get(domain + attack)
    
    # Kiểm tra xem response có chứa dấu hiệu của lỗ hổng SQL Injection không
    if "SQL syntax" in response.text:
        # Nếu dấu hiệu của lỗ hổng được phát hiện, in ra thông điệp cảnh báo và chuỗi tấn công
        print("SQL Injection vulnerability detected with attack:", attack)
