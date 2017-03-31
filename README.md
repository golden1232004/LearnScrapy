
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


A Simple Case:
==============

* scrapy runspider quotes_spider.py -o quotes.json

  * 定义默认的callback
  * 跟踪链接的使用方法

A Project -- Tutorial:
======================

* cd tutorial root directory
* scrapy crawl quotes -o quotes.json

A Poject -- tow spiders:
========================

* quotesbot


A Project -- tmSpider
=====================

* combine with selenium + phantomjs

Reference
========

1. [关于“淘宝爆款”的数据抓取与数据分析](http://blog.csdn.net/u012150179/article/details/37306629)