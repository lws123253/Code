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
    





#_*_ coding:UTF-8 _*_

import requests
from bs4 import BeautifulSoup
def get_movies():
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Host':'movie.douban.com'
    }
    movie_list=[]
    for i in range(0,10):
        link='https://movie.douban.com/top250?start='+str(i*25)
        r=requests.get(link,headers=headers,timeout=10)
        print (str(i+1),'页码响应状态码：',r.status_code)
        soup=BeautifulSoup(r.text,'lxml')
        div_list=soup.find_all('div',class_='hd')
        for each in div_list:
           # movie=each.a.span.text.strip()
            movie=each.a.contents[3].text.strip()
            movie=movie[2:]
            movie_list.append(movie)
            #print(each.a.contents[3].text.strip())
    return movie_list
movies=get_movies()
print(movies)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




