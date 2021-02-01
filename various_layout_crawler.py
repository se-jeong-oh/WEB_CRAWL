import requests
from bs4 import BeautifulSoup


class Content:
    """
    글/페이지 전체에 사용할 기반 클래스
    """
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        출력 결과를 원하는 대로 바꿀 수 있는 함수
        """
        print('Title: {}'.format(self.title))
        print('URL: {}'.format(self.url))
        print(self.body)

class Website:
    """
    웹사이트 구조에 관한 정보를 저장할 클래스
    """

    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Crawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):
        """
        Beautiful 객체와 선택자를 받아 콘텐츠 문자열을 추출하는 함수
        주어진 선택자로 검색된 결과가 없다면 빈 문자열을 반환합니다.
        :param pageObj:Beautifulsoup 객체
        :param selector:선택자, Website 객체 요소
        :return:문자열
        """

        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join(
                [elem.get_text() for elem in selectedElems]
            )
        return ''

    def parse(self, site, url):
        """
        URL을 받아 콘텐츠를 추출합니다.
        :param site: Website 객체
        :param url: URL
        :return:
        """
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()

crawler = Crawler()

siteData = [
    ['0\'Reilly Media', 'http://oreilly.com',
        'h1', 'p.t-promo'],
    ['Brookings', 'http://www.brookings.edu',
        'h1', 'div.post-body']
]

websites = []
urls = [
    'http://shop.oreilly.com/product/0636920028154.do',
    'https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/'
]
for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))

crawler.parse(websites[0], urls[0])
crawler.parse(websites[1], urls[1])