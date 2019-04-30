#_*_ coding:UTF-8 _*_

import requests
from bs4 import BeautifulSoup
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36','Host':'movie.douban.com'}
mylink='https://movie.douban.com/top250?start='

for s in range(0,11):
    link=mylink+str(s*25)
    r=requests.get(link,headers=headers)
    s=BeautifulSoup(r.text,'lxml')
    div_list=s.find_all('div',class_='hd')
    
    for each in div_list:
        movie=each.a.span.text.strip()
        with open('D:\\title.txt','a+') as f:
            f.write(movie+'\n')