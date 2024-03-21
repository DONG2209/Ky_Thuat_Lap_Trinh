# Import module dns.resolver để thực hiện các thao tác liên quan đến DNS
import dns.resolver

# Danh sách các tên miền cần truy vấn
hosts = ['google.com', 'microsoft.com', 'facebook.com']

# Lặp qua từng tên miền trong danh sách
for host in hosts:
    print("Host:", host)  # in ra tên miền 
    try:
        # Lấy địa chỉ IPv4 (A)
        ipv4_answers = dns.resolver.resolve(host, 'A')
        for ipv4_answer in ipv4_answers:
            print("IPv4:", ipv4_answer)

        # Lấy địa chỉ IPv6 (AAAA)
        ipv6_answers = dns.resolver.resolve(host, 'AAAA')
        for ipv6_answer in ipv6_answers:
            print("IPv6:", ipv6_answer)

        # Lấy thông tin máy chủ thư (Mail Exchange)
        mx_records = dns.resolver.resolve(host, 'MX')
        for mx_record in mx_records:
            print("MX:", mx_record.exchange)

    # Xử lý ngoại lệ khi không tìm thấy bản ghi A, AAAA hoặc MX
    except dns.resolver.NoAnswer:
        print("No A, AAAA, or MX record found")
