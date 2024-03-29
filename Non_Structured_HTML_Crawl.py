from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html1 = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs1 = BeautifulSoup(html1, 'html.parser')
nameList = bs1.findAll('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())
# 특정 태그와 id 검색하는 findAll 함수

html2 = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs2 = BeautifulSoup(html2, 'html.parser')
for child in bs2.find('table', {'id': 'giftList'}).children:
    print(child)
for child in bs2.find('table', {'id': 'giftList'}).descendants:
    print(child)
# 자식(child)과 자손(descendants)의 차이

for sibling in bs2.find('table', {'id': 'giftList'}).tr.next_siblings:
    print(sibling)
# 형제 찾기

print(bs2.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
# 부모를 통해 역트리방향으로 탐색

images = bs2.findAll('img', {'src': re.compile('\.\./img/gifts/img.*\.jpg')})  # 정규표현식을 이용한 상대경로 탐색
for img in images:
    print(img.attrs['src'])  # myTag.attrs 로 파이썬 딕셔너리 형태의 객체에 대해 원하는 속성에 접근 가능

print(len(bs1.findAll(lambda tag: tag.get_text() == 'Anna Pavlovna')))  # 람다 함수를 이용하여 해당 text가 몇 번 나오는 지 탐색
