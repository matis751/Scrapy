import scrapy
import os
from properties.items import PropertiesItem

def parse_url(self, response):


class BasicSpider(scrapy.Spider):
    name = 'basic'
    def __init__(self):
    allowed_domains = ['web']
    self.start_urls = ["https://fr.muzeo.com/categorie/peinture/contemporain/"] 
    self.url = response.xpath('//*[@]')


    def parse(self, response):
        item = PropertiesItem()
        item['title'] = response.xpath('//*[@class="title_oeuvre"]/text()').extract()
        item['price'] = response.xpath('//*[@currency="eur_ttc"]/text()').extract()
        item['image_urls'] =  response.xpath('//*[@class="oeuvre_img lazy reproduction_class"]/@data-src').extract()
        return item
