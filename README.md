
Environment:
============

```
Scrapy    : 1.3.2
lxml      : 3.6.4.0
libxml2   : 2.9.2
cssselect : 1.0.1
parsel    : 1.1.0
w3lib     : 1.17.0
Twisted   : 17.1.0
Python    : 2.7.12 |Anaconda custom (64-bit)| (default, Jul  2 2016, 17:42:40) - [GCC 4.4.7 20120313 (Red Hat 4.4.7-1)]
pyOpenSSL : 16.2.0 (OpenSSL 1.0.2j  26 Sep 2016)
Platform  : Linux-4.4.0-57-generic-x86_64-with-debian-stretch-sid
```

Frameworks:
==========

Learn
-----

1. a simple case

* scrapy runspider quotes_spider.py -o quotes.json
  * 定义默认的callback
  * 跟踪链接的使用方法

2. tutorial

* cd tutorial root directory
* scrapy crawl quotes -o quotes.json

3. two spiders:

* quotesbot


Spiders
-------

1. tmSpider

> combine with selenium + phantomjs to crawl tmall or taobao data

* **Search**: input keys to search products
* **Extract**: shopUrl, category(店铺分类), name(店铺名)， nick(卖家昵称), nid（店铺ID）, provcity（店铺区域）, totalsold（店铺宝贝）, procnt（店铺销量）, startFee, mainAuction（店铺关键词）, userRateUrl（用户评分链接）, sgr（店铺好评率）, srn（店铺等级）, mas（描述相符）, sas（服务态度）, cas（物流速度）
* **Storage**: insert to database, such as mongodb


Data Analysis
-------------

* TODO




Reference
========

1. [关于“淘宝爆款”的数据抓取与数据分析](http://blog.csdn.net/u012150179/article/details/37306629)