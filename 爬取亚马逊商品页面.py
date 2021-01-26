import requests
url = "https://www.amazon.cn/gp/product/B00W2T39C8/ref=cn_ags_s9_asin?pf_rd_p=33e63d50-addd-4d44-a917-c9479c457e1a&pf_rd_s=merchandised-search-3&pf_rd_t=101&pf_rd_i=1403206071&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=FQQGZ7T42BF03V117HRD&pf_rd_r=FQQGZ7T42BF03V117HRD&pf_rd_p=33e63d50-addd-4d44-a917-c9479c457e1a&ref=cn_ags_s9_asin_1403206071_merchandised-search-3"
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url,headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")