import urllib.request
from urllib.request import Request


url = "https://actvn.edu.vn/"  # URL của trang web truy cập
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36"
# User-Agent của trình duyệt, ở đây là của Google Chrome trên Windows

def chrome_user_agent():
    opener=urllib.request.build_opener()
    opener.addheaders=[("User-Agent",USER_AGENT)]
    urllib.request.install_opener(opener)
    respone=urllib.request.urlopen(url)
    print("Response headers:")  # In ra tiêu đề của response
    for header,value in respone.getheaders():
        print(header,":",value)

if __name__ == "__main__":
    chrome_user_agent()
