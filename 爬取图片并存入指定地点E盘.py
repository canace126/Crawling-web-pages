import requests
import os
url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1533128040259&di=601acd33bcb188bfeb41cb50bc51ed41&imgtype=0&src=http%3A%2F%2Fs1.sinaimg.cn%2Fmw690%2F006LDoUHzy7auXElZGE40%26690"
path = "E://hh/abc.jpg"
try:
    
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件已保存")
       
except :
    print("爬取失败")