# -*- coding: utf-8 -*-
import time
import scrapy


class TmallSpider(scrapy.Spider):
    name = "tmall"
    allowed_domains = ["tmall.com"]
    start_urls = [
        'https://www.taobao.com'
    ]
    
    def parse(self, response):
        html = response.body
        print("----------------------------------------------------------------------------")
        value = response.xpath("//title/text()").extract()
        if len(value) > 0:
            print value[0]
        else:
            print "can not find title"
        #print html

        values = response.xpath("//dt[@class='tb-metatit']/text()")
        print values

        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        # extra=gsextractor.GsExtractor()
        # extra.setXsltFromAPI("31d24931e043e2d5364d03b8ff9cc77e", "淘宝天猫_商品详情30474","tmall","list")

        # result = extra.extract(html)
        # print(str(result).encode('gbk','ignore').decode('gbk'))
        #file_name = 'F:/temp/淘宝天猫_商品详情30474_' + self.getTime() + '.xml'
        #open(file_name,"wb").write(result)
