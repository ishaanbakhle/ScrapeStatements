# -*- coding: utf-8 -*-
import scrapy


class PropubSpider(scrapy.Spider):
    name = 'propub'
    allowed_domains = ['https://projects.propublica.org/represent/statements/search?q=%22climate+change%22']
    start_urls = ['https://projects.propublica.org/represent/statements/search?q=%22climate+change%22']

    def parse(self, response):
        self.log('I just visited ' +  response.url)
        yield{
            'Table': response.css('tr').extract()
        }
