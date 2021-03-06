import requests
from bs4 import BeautifulSoup as BSoup
import json
url = r'http://fanyi-api.baidu.com/api/trans/product/apidoc'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}
r =  requests.get(url,headers=headers) # 获取网页
if r.status_code == 200:
    r.encoding = r.apparent_encoding
    bs = BSoup(r.text)
    tables = bs.findAll('table','info-table') # 提取数据
    table = tables[2].findAll('td')
    keys=[]
    values=[]
    for i in range(0,len(table),2):  # 数据放在Python对象中
        keys.append(table[i].text)
        values.append(table[i+1].text)
    print(keys)
    print(values)
    d=dict(zip(keys,values)) # 数据放在字典中
    with open('languages.json', 'w+') as f: # 存入json文件中
        json.dump(d, f)
# 下面是读取json文件
# d1 = {}
# with open('languages.json', 'r') as f:
#         d1=json.load(f)