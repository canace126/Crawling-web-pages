import requests
keyword = "Python"
try:
    kv = {'wd':keyword}#如果用360就将键值对wd改成q将baidu改成so
    r = requests.get("http://www.baidu.com/s",params = kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("爬取失败")