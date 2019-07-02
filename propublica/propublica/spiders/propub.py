# -*- coding: utf-8 -*-
import scrapy
import numpy as np


class PropubSpider(scrapy.Spider):
    name = 'propub'
    allowed_domains = ['https://projects.propublica.org']
    start_urls = ['https://projects.propublica.org/represent/statements/search?q=%22climate+change%22']
    num_pages = 155
    for i in np.arange(2, num_pages+1):
        start_urls.append('https://projects.propublica.org/represent/statements/search?' + 'page=' + str(i) + 'q=%22climate+change%22')
    start_urls[1]

    def parse(self, response):
        self.log('I just visited ' +  response.url)
        yield{
            'Table': response.css('tr').extract()
        }
