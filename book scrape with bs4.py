#!/usr/bin/env python
# coding: utf-8

# In[24]:


import requests 
from bs4 import BeautifulSoup as bs4
import pandas as pd

pages = []
prices = []
stars = []
titles = []
urls = []

page_to_scrape = 1

for i in range(1,page_to_scrape+1):
    url = 'http://books.toscrape.com/catalogue/page-{}.html'.format(i)
    pages.append(url)
for item in pages:
    page = requests.get(item)
    soup = bs4(page.text, 'html.parser')
    for i in soup.findAll('h3'):
        title = i.getText()
        titles.append(title)
    for i in soup.findAll('p',class_ = 'price_color'):
        price = i.getText()
        prices.append(price)
    for s in soup.findAll('p', class_ = 'star-rating'):
        for k,v in s.attrs.items():
            star = v[1]
            stars.append(star)
    divs = soup.findAll('div', class_ = 'image_container')
    
    for thumbs in divs:
        tgs = thumbs.find('img', class_ = 'thumbnail')
        urlss = 'http://books.toscrape.com/' + str(tgs['src'])
        #print(urlss)
        newurls = urlss.replace('../','')
        urls.append(newurls)

    
    


# In[25]:


data = {'title':titles,'price':prices,'rating':stars,'url':urls}
data


# In[26]:


df = pd.DataFrame(data = data)


# In[27]:


print(df)


# In[ ]:




