# Import module nmap để sử dụng trong việc quét cổng
import nmap

# Tạo một đối tượng portScanner từ module nmap để thực hiện quét cổng
portScanner = nmap.PortScanner()

# Địa chỉ host muốn kiểm tra cổng, ở đây là 'dantri.com.vn'
host_scan = 'dantri.com.vn'

# Danh sách các cổng quét
port_list = "21,22,23,25,80"

# Thực hiện quét cổng trên máy chủ đã cho, sử dụng tùy chọn -n để không thực hiện phân giải DNS và -p để chỉ định danh sách cổng
portScanner.scan(hosts=host_scan, arguments='-n -p ' + port_list)

# In ra dòng lệnh đã sử dụng để thực hiện quét cổng
print(portScanner.command_line())

# Tạo một danh sách các host và trạng thái của host từ kết quả quét
hosts_list = [(x, portScanner[x]['status']['state']) for x in portScanner.all_hosts()]

# In ra danh sách host và trạng thái của host
for host, status in hosts_list:
    print(host,':',status)

# Lặp qua tất cả các giao thức được phát hiện trong kết quả quét
for protocol in portScanner[host].all_protocols():
    print('Protocol : %s' % protocol)
    # Lặp qua danh sách các cổng TCP và in ra trạng thái của mỗi cổng
    list_ports = portScanner[host]['tcp'].keys()
    for port in list_ports:
        print('Port : %s\tState : %s' % (port, portScanner[host][protocol][port]['state']))
