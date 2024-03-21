import shodan

# Thay đổi 'YOUR_API_KEY' bằng API key của bạn từ trang web Shodan Developer
API_KEY = 'lp6o7Ve0HG4mxypTuoAH9QFisBC3abLq'

def get_ip_info(ip):
    try:
        # Khởi tạo đối tượng Shodan với API key
        api = shodan.Shodan(API_KEY)
        
        # Lấy thông tin về địa chỉ IP từ Shodan
        ip_info = api.host(ip)
        
        # In ra thông tin
        print(f"IP: {ip_info['ip_str']}")
        print(f"Organization: {ip_info.get('org', 'N/A')}")
        print(f"Country: {ip_info.get('country_name', 'N/A')}")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"Latitude: {ip_info.get('latitude', 'N/A')}")
        print(f"Longitude: {ip_info.get('longitude', 'N/A')}")
        print("Ports:")
        for port_info in ip_info['data']:
            print(f"- Port: {port_info['port']} ({port_info.get('transport', 'N/A')})")
            print(f"  Service: {port_info.get('service', 'N/A')}")
            print(f"  Banner: {port_info.get('banner', 'N/A')}")
            print()
    except shodan.APIError as e:
        print(f"Error: {e}")

# Thay đổi địa chỉ IP cần tìm kiếm thông tin
ip_to_search = '1.1.1.1'
get_ip_info(ip_to_search)
