import scrapy
from G_market_2.items import GMarket2Item

keyword = input('찾고싶은 키워드를 입력해주세요: ')

while True:
    print('G마켓랭크순, 8. 판매인기순, 1. 낮은가격순, 2. 높은가격순, 13. 상품명많은순, 3. 신규상품순')
    array = input('원하는 정렬 방법을 선택하세요: ')
    if array == '8' or array == '1' or array == '2' or array == '13' or array == '3': 
        break

if array == '8':
    array_type = '판매인기순'
if array == '1':
    array_type = '낮은가격순'
if array == '2':
    array_type = '높은가격순'
if array == '13':
    array_type = '상품명많은순'
if array == '3':
    array_type = '신규상품순'

URL = ['https://browse.gmarket.co.kr/search?keyword='+keyword+'&f=d:f&s='+array]


class Gmarket2Spider(scrapy.Spider):
    name = 'gmarket_2'
    start_urls = [URL]

    def parse(self, response):
        global url

        for i in range(1, 101):

            URL = response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]/div[1]/div[2]/div[1]/div[2]/span/a')
            div = response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]')

            if (URL != []):
                href = div.xpath('./div[1]/div[2]/div[1]/div[2]/span/a/@href')
                url = response.urljoin(href[0].extract())
                yield scrapy.Request(url, callback = self.parse_page_content1)
                
            if (URL == []):
                href = div.xpath('./div[1]/div[2]/div[1]/div[1]/span/a/@href')
                url = response.urljoin(href[0].extract())
                yield scrapy.Request(url, callback = self.parse_page_content1)

    def parse_page_content1 (self, response):
        item = GMarket2Item()
        item['Array'] = array_type
        item['Item'] = response.xpath('//*[@id="itemcase_basic"]/div/h1/text()')[0].extract()
        item['Price'] = response.xpath('//*[@id="itemcase_basic"]/div/p/span/strong/text()')[0].extract()
        item['URL'] = url
        return item
            
    def parse_page_content2 (self, response):
        item = GMarket2Item()
        item['Array'] = array_type
        item['Item'] = response.xpath('//*[@id="itemcase_basic"]/div/h1/text()')[0].extract()
        item['Price'] = response.xpath('//*[@id="itemcase_basic"]/div/p/span/strong/text()')[0].extract()
        item['URL'] = url
        return item
