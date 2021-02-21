import scrapy


def generate_start_urls():
    names = ['Alice', 'Bob']
    quests = ['Hi', 'My Friend']
    
    return ['http://pythonscraping.com/linkedin/formAction.php?name{}&quest={}&color=blue'.format(name, quest) for name in names for quest in quests]
class GetFormSpider(scrapy.Spider):
    name = 'get_form'
    allowed_domains = ['pythonscraping.com']
    start_urls = generate_start_urls()

    def parse(self, response):
        return {'text': response.xpath('//div[@class="wrapper"]/text()').get()}
        
