from lxml import html
import requests


url = 'https://news.mail.ru/politics/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 '
    'Safari/537.36',
}

response = requests.get(url, headers=headers)

dom = html.fromstring(response.text)

news = dom.xpath("//div[@class='newsitem newsitem_height_fixed js-ago-wrapper js-pgng_item']")

news_dict = {}

for new in news:
    new_link = new.xpath("./span/a/@href")[0]
    new_name = new.xpath("./span/a/span[@class='newsitem__title-inner']/text()")[0]
    res_name = new.xpath("./div/span[@class='newsitem__param']/text()")[0]
    new_data = new.xpath("./div/span[@class='newsitem__param js-ago']/@datetime")[0]
    news_dict[new_link] = {
        'name': new_name,
        'res': res_name,
        'data': new_data,
    }

print(news_dict)


