import scrapy

from tutorial.items import TutorialItem

class DmozSpider(scrapy.Spider):
    # 必须定义
    name = "dmoz"
    # 初始urls
    start_urls = [
        "http://www.baidu.com"
    ]

    # 默认response处理函数
    def parse(self, response):
        # 把结果写到文件中
      '''  filename = 'E:/a.text'
        f = open(filename,'wb')
        f.write(response.body)
        print(response.body)'''
      for sel in response.xpath('/html/head/title'): #xpath语句的异常，一开始/html/head/title/报错 需要去掉最后的/
          print(sel)
          title = sel.xpath('text()').extract()
          item = TutorialItem()
          item['title'] = title[0]
          print('title=',title)
          yield item

