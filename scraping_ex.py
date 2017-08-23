# -*- coding: utf-8 -*-

import requests
# 언어의 온도 페이지의 URL = http://www.yes24.com/24/goods/30387696
r = requests.get('http://www.yes24.com/24/goods/30387696')
html = r.text
#html 변수에 http://www.yes24.com/24/goods/30387696 페이지에 해당 하는 소스 코드 정보가 담겨져 있다.


from bs4 import BeautifulSoup
# BeautifulSoup을 통해서 원하는 정보가 담겨져 있는 tag에 접근하고, 해당 정보를 추출한다.
soup = BeautifulSoup(html, 'lxml')
span_tag = soup.find('h2', attrs={'class':'gd_name'})
title = span_tag.text
print(title) 

