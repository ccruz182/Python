import scrapy
from scrapy.http import FormRequest


class GetFormSpider(scrapy.Spider):
    name = 'get_form'
    allowed_domains = ['pythonscraping.com']

    def start_requests(self):
        names = ['Alice', 'Bob']
        quests = ['Hi', 'My Friend']
    
        return [FormRequest('http://pythonscraping.com/linkedin/formAction.php', formdata={'name': name, 'quest': quest, 'color': 'red'}, callback=self.parse) for name in names for quest in quests]

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}
        
