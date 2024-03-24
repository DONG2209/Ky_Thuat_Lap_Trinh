import nmap
import xml.etree.ElementTree as ET

class NmapScanner():
    def __init__(self):
        # Khởi tạo đối tượng PortScanner từ thư viện nmap
        self.portScanner = nmap.PortScanner()
    
    def nmapScan(self, ip_address, port):
        # Thực hiện quét cổng trên địa chỉ IP được cung cấp
        self.portScanner.scan(ip_address, port)
        # In ra lệnh quét được thực thi
        print("[+] Executing command:", self.portScanner.command_line())

        # Xử lý kết quả trả về từ Nmap
        xml_output = self.portScanner.get_nmap_last_output()
        root = ET.fromstring(xml_output)

        # Lặp qua các phần tử host trong kết quả XML
        for host in root.findall('host'):
            # Lặp qua các cổng trong phần tử ports
            for port in host.find('ports').findall('port'):
                # Lấy số cổng và trạng thái của nó
                port_number = port.get('portid')
                state = port.find('state').get('state')
                print(f"Port {port_number}: {state}")

def main():
    # Nhập địa chỉ IP cần quét từ người dùng
    ip_address = input("ip scan: ")
    # Danh sách các cổng cần quét
    ports = ['21', '22', '23', '25', '80', '443']
    # Quét từng cổng và in kết quả
    for port in ports:
        NmapScanner().nmapScan(ip_address, port)

if __name__ == "__main__":
    main()


# 42.113.206.26