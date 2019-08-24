# 函数方法集
from bs4 import BeautifulSoup
from socket import gethostbyname
from hashlib import md5
import requests
from urllib.parse import urlparse
from requests.utils import get_encodings_from_content


# 获取url.域名
def GetHost(url):
    try:
        return urlparse(url).hostname
    except:
        return None

# 获取url.IP
def GetIP(host):
    try:
        return gethostbyname(host)
    except:
        return None


# Hash算法MD5实现
def MD5(str):
    hl = md5()
    hl.update(str.encode(encoding='utf8'))
    return hl.hexdigest()


# 模拟访问url返回response
def Response(url):
    header = {
            'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
            }
    try:
        response = requests.Session().get(url, headers=header, timeout=30)
    except:
        return None
    charset = requests.utils.get_encodings_from_content(response.text)
    if charset:
        charset = charset[0]
    else:
        charset = response.apparent_encoding
    if charset[0:2]=='gb':
        response.encoding='gb18030'
    else:
        response.encoding = charset
    return response


# 将response生成bsobj
def bsObj(response):
    try:
        return BeautifulSoup(response.text,'lxml')
    except:
        return None
