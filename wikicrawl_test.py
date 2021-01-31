from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find('div', {'id':'bodyContent'}).findAll('a', {'href': re.compile('^(/wiki/)((?!:).)*$')}):
    if 'href' in link.attrs:
        print(link.attrs['href'])
#id가 bodyContent인 div 안의 정규표현식을 이용해서 다른 항목을 가리키는 모든 링크 탐색

