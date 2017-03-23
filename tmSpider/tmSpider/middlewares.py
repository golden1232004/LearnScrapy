# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import time
from scrapy.exceptions import IgnoreRequest
from scrapy.http import HtmlResponse, Response
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from lxml import etree

class CustomDownloader(object):
    def __init__(self):
        # use any browser you wish
        cap = webdriver.DesiredCapabilities.PHANTOMJS
        cap["phantomjs.page.settings.resourceTimeout"] = 1000
        cap["phantomjs.page.settings.loadImages"] = True
        cap["phantomjs.page.settings.disk-cache"] = True
        cap["phantomjs.page.customHeaders.Cookie"] = 'SINAGLOBAL=3955422793326.2764.1451802953297; '
        self.driver = webdriver.PhantomJS(desired_capabilities=cap)
        #wait = ui.WebDriverWait(self.driver,10)

    def VisitPersonPage(self, url):
        print('正在加载网站.....')
        self.driver.get(url)
        time.sleep(1)
        # 翻到底，详情加载
        #js="var q=document.documentElement.scrollTop=10000"
        js = "window.scrollTo(0, document.body.scrollHeight);"
        self.driver.execute_script(js)
        delay = 20 # seconds
        try:
            wait = WebDriverWait(self.driver, delay)
            element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "screen-outer clearfix")))
        except TimeoutException:
            print "Loading took too much time!"
        except WebDriverException, e:
            print e.message

        # 使用self.driver.find_elements_by_xpath("//title")[0].text无法找到。不知道为什么。
        content = self.driver.page_source.encode('utf-8')
        self.driver.get_screenshot_as_file("screenshot.jpg") #通过截屏发现访问的页面
        # page_tree = etree.HTML(content)
        # title_ = page_tree.xpath("//title/text()")
        # print ".................................."
        # if len(title_) > 0:
        #     print title_[0]
        # else:
        #     print "没有找到名称"

        print('网页加载完毕.....')
        return content

    def __del__(self):
        self.driver.quit()

class CustomMiddlewares(object):
    def process_request(self, request, spider):
        url = str(request.url)
        print "url:%s"%url
        dl = CustomDownloader()
        content = dl.VisitPersonPage(url)
        return HtmlResponse(url, encoding='utf-8', status = 200, body = content)

    def process_response(self, request, response, spider):
        if len(response.body) == 100:
            return IgnoreRequest("body length == 100")
        else:
            return response


class TmspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
