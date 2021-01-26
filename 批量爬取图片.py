import requests
from bs4 import BeautifulSoup
import urllib.request


x = 0
def GetImg():
    response = requests.get('http://www.mzitu.com/zipai/comment-page-2')
    re = response.text
    #创建对象，解析网页
    soup = BeautifulSoup(re,'html.parser')
    #找到img标签
    girl = soup.find_all('img')
    for i in girl:
        global x
        imgl=i.get('src')
        urllib.request.urlretrieve(imgl,'E:/python/xiuxiu/%s.jpg'%x)
        x+=1
        print("正在下载第%x张图片"%x)
        
def getHtml(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
    page1=urllib.request.Request(url,headers=headers)
    page=urllib.request.urlopen(page1)

    html=page.read()
    
GetImg()    