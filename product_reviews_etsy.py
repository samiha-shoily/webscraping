from selenium import webdriver
import pandas as pd
import time

PATH = 'chromedriver.exe'
driver = webdriver.Chrome(PATH)

refUrl = 'https://www.etsy.com/shop/{shopname}/reviews?ref=pagination&page='
shopName = input('shop_name=?')
pageNumber = int(input('page_number=?'))
fileName = input('output_file_name =?')
url = refUrl.format(shopname= shopName)
names = []
links = []

for i in range(1, pageNumber+1):
    url1 = url+str(i)
    driver.get(url1)
    time.sleep(2)
    all_reviews = driver.find_elements_by_css_selector('ul.reviews-list')
    for reviews in all_reviews:
        for review in reviews.find_elements_by_css_selector('.pb-xs-0'):
            name = review.find_elements_by_css_selector('.shop2-review-attribution')[0].text
            names.append(name)
            link = review.find_elements_by_css_selector('div.col-xs-12.col-lg-10.listing-group.pl-xs-0.pr-xs-0 a')[0].get_attribute('href')
            links.append(link)


records = {'Name': names, 'Links': links}
df = pd.DataFrame(records, columns=['Name', 'Links'])
df.to_excel(fileName+'.xlsx')
driver.close()