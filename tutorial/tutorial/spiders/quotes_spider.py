import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"  # identifies the Spider. It must be unique within a project
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]
    #################################################################################
    # default callback
    # response [in]: page content
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page) # builds a full absolute URL using the urljoin() method (since the links can be relative)
            yield scrapy.Request(next_page, callback=self.parse)
