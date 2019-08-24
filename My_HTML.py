from bs4 import BeautifulSoup
from w3lib.html import remove_tags
from socket import gethostbyname
from urllib.parse import urlparse
import requests


class MyHTML:
    def __init__(self,url=None):
        self.url=url
        self.host=Host(self.url)
        self.ip=IP(self.host)
        self.response=Response(self.url)
        try:
            self.bs=BS(self.response.text)
            self.html=str(self.bs)
        except:
            self.bs=None
            self.html=None
        self.text=Text(self.html,self.bs)

    def reset(self,url=None):
        self.url=url
        self.host=Host(self.url)
        self.ip=IP(self.host)
        self.response=Response(self.url)
        try:
            self.bs=BS(self.response.text)
            self.html=str(self.bs)
        except:
            self.bs=None
            self.html=None
        self.text=Text(self.html,self.bs)


def Host(url):
    try:
        return urlparse(url).hostname
    except:
        return None


def IP(host):
    try:
        return gethostbyname(host)
    except:
        return None


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


def BS(resText):
    try:
        return BeautifulSoup(resText,'html.parser')
    except:
        return None


def Text(html,bsobj=None):
    if bsobj is None:
        bsobj = BS(html)
    try:
        for tags in ['script','style']:
            for tag in bsobj.find_all(tags):
                html = html.replace(str(tag), '')
        html = ' '.join(remove_tags(html).split())
        return html
    except:
        return None


# 演示
def demo():
    obj = MyHTML('http://lib.njnu.edu.cn/')
    # print(type(obj))
    print(obj.url)
    print(obj.host)
    print(obj.ip)
    print(obj.response)
    print(obj.bs)
    print(obj.html)
    print(obj.text)
    obj.reset('http://localhost/')
    print(obj.url)
    print(obj.host)
    print(obj.ip)
    print(obj.response)
    print(obj.bs)
    print(obj.html)
    print(obj.text)

if __name__ == "__main__":
    demo()
