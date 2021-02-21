import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        #title = response.css('span.title::text').get()
        data_page = {
            'author': response.xpath("//pre/span[@class='author-name']/text()").get(),
            'company': response.xpath("//span[@class='author-company']/text()").get(),
            'rfc': response.xpath("//span[@class='rfc-no']/text()").get(),
            'date': response.xpath("//span[@class='date']/text()").get(),
            'information': response.xpath("//div[@class='text']").get(),
        }
        
        return data_page
