import scrapy

class QuoteSpider(scrapy.Spider):
  name: 'quotes'
  def start_requests(self):
    urls = [
       'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse)