import requests
import os

# Lấy khóa API Shodan từ biến môi trường
SHODAN_API_KEY = os.environ.get('SHODAN_API_KEY')

def get_shodan_info(ip):
    try:
        # kiểm khóa API được cung cấp chưa 
        if SHODAN_API_KEY is None:
            raise ValueError("Thieu khoa API Shodan")

        # Gọi API Shodan để lấy thông tin về địa chỉ IP
        response = requests.get(f'https://api.shodan.io/shodan/host/{ip}?key={SHODAN_API_KEY}')
        response.raise_for_status()  # Ném một ngoại lệ cho các phản hồi không tốt (ví dụ: 404)

        # Phân tích phản hồi JSON
        results = response.json()
        return results
    except requests.RequestException as e:
        return f"loi khi tai dl: {e}"
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"loi khong mong muon: {e}"

ip = '1.1.1.1'
print(get_shodan_info(ip))

# set SHODAN_API_KEY=lp6o7Ve0HG4mxypTuoAH9QFisBC3abLq
