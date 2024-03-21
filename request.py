import requests  # Import thư viện requests để thực hiện yêu cầu HTTP

url = "https://actvn.edu.vn/"  # URL của trang web truy cập
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36"
# User-Agent của trình duyệt, ở đây là của Google Chrome trên Windows

def chrome_user_agent():
    try:
        # Tạo một yêu cầu HTTP sử dụng phương thức GET đến URL đã chỉ định và thiết lập User-Agent
        request = requests.Request("GET", url, {"User-Agent": USER_AGENT})
        
        print("Requests headers :")  #
        for header, value in request.headers.items():  # Lặp qua tất cả các tiêu đề trong yêu cầu
            print(header, ":", value)  # In ra mỗi tiêu đề và giá trị của nó
    except requests.exceptions.RequestException as e:  # Xử lý các ngoại lệ có thể xảy ra khi gửi yêu cầu
        print("Error:", e)  # In ra thông báo lỗi nếu có

if __name__ == "__main__":
    chrome_user_agent()  # Gọi hàm chrome_user_agent() để thực hiện việc tạo và kiểm tra yêu cầu HTTP
