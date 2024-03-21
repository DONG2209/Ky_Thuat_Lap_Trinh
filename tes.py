import requests
import os

# Lấy khóa API Shodan từ biến môi trường
SHODAN_API_KEY = os.environ.get('SHODAN_API_KEY')

def search_anonymous_ftp():
    try:
        # Đảm bảo rằng khóa API được cung cấp
        if SHODAN_API_KEY is None:
            raise ValueError("Thieu khoa API Shodan")

        # Gọi API Shodan để tìm kiếm các máy chủ FTP đăng nhập ở chế độ Anonymous
        query = 'ftp anonymous login'
        response = requests.get(f'https://api.shodan.io/shodan/host/search?key={SHODAN_API_KEY}&query={query}')

        # Phân tích phản hồi JSON
        results = response.json()

        # Lấy danh sách các địa chỉ IP
        ip_list = [result['ip_str'] for result in results['matches']]
        return ip_list
    except requests.RequestException as e:
        return f"loi khi tai dl: {e}"
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"loi khong mong muon: {e}"

# Thực hiện tìm kiếm và in ra danh sách địa chỉ IP
print("Danh sach đia chi IP  Anonymous:")
print(search_anonymous_ftp())
