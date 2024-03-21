import requests

url = "https://actvn.edu.vn/"    # URL của trang web truy cập

def get_response_headers(url):
    try:
        response = requests.head(url)  # Gửi một yêu cầu HEAD đến URL để chỉ lấy thông tin về header của response
        
        print("Response headers:")  # In ra tiêu đề của response
        for header, value in response.headers.items():  # Lặp qua tất cả các tiêu đề trong response headers
            print(header, ":", value)  # In ra mỗi tiêu đề và giá trị của nó
    except requests.exceptions.RequestException as e:  # Xử lý các ngoại lệ có thể xảy ra khi gửi yêu cầu
        print("Error:", e)  # In ra thông báo lỗi nếu có

if __name__ == "__main__":
    get_response_headers(url)  # Gọi hàm để lấy response headers của URL đã cho
