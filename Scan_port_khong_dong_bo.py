# class PortScannerAsync(object):
#     def __init__(self):
#         self._process = None
#         self._nm = nmap.PortScanner()
#         return
    
#     def __del__(self):
#         if self._process is not None:
#             self._process.terminate()

import nmap

# Định nghĩa hàm gọi lại để xử lý kết quả quét
def callback_result(host, scanner_result):
    print(host, scanner_result)

if __name__ == '__main__':
    # Tạo một phiên bản của PortScannerAsync

    # Khởi tạo nmap PortScannerAsync
    portScannerAsync = nmap.PortScannerAsync()

    # Quét các cổng khác nhau một cách không đồng bộ trên máy chủ mục tiêu 'scanme.nmap.org'
    portScannerAsync.scan(hosts='scanme.nmap.org', arguments='-p 21', callback=callback_result)
    portScannerAsync.scan(hosts='scanme.nmap.org', arguments='-p 22', callback=callback_result)
    portScannerAsync.scan(hosts='scanme.nmap.org', arguments='-p 23', callback=callback_result)
    portScannerAsync.scan(hosts='scanme.nmap.org', arguments='-p 25', callback=callback_result)
    portScannerAsync.scan(hosts='scanme.nmap.org', arguments='-p 80', callback=callback_result)

    # Kiểm tra xem quá trình quét vẫn đang diễn ra hay không
    while portScannerAsync.still_scanning():
        print("Scanning >>>")
        # Chờ 5 giây trước khi kiểm tra lại
        portScannerAsync.wait(5)

