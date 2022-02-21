import requests
from bs4 import BeautifulSoup

import re

import pandas as pd

target_url = "https://www.ja-chiba.or.jp/contents/detail/id=79"

res = requests.get(target_url)
soup = BeautifulSoup(res.text, 'html.parser')

t_tag1 = "c-article p-news__contents"

d1 = soup.find('main', class_=t_tag1)
#通称を取得する
# d1 = soup.find("h3")

#liタグのものを取得
d2 = d1.find_all('li')
d3 = [i.text for i in d2]

#\r\n\tを:に変換
d4 = [i.replace('\r\n\t',':') for i in d3]
#改行文字等を成形、削除
d5 = [re.sub(r"[\n,\u3000]","",i) for i in d4]
#キャラクターを削除
jas1 = []
for i in d5:
    if '正式名称' in i or '住所' in i or '管内の市町村' in i :
        jas1.append(i)

jas2 = [i.split(':') for i in jas1]

df = pd.DataFrame(jas2)
df.to_csv('chiba_jas.csv')
