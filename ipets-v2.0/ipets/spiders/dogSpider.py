import scrapy
import re
from ipets.items import IpetsItem
"""
爬虫类 负责到互联网下载数据 分析数据 然后输出到pipeline中 在pipeline再做数据保持的处理
"""
class DogSpider(scrapy.Spider):
    name = "dog"

    start_urls = [
        "http://www.dog126.com/ggjs.html"
    ]


    def parse(self, response):
       # print(response.body)
        divlist = response.xpath('//div[@class="jieshao"]')
        for res in divlist:
            #print(res)
            #提取href值
            href = res.xpath('dl/dt/a/@href').extract()
           # print(href)
            #再次根据url调用 返回数据
            #生成请求，将新的url加入到爬取队列中，cl为url，callback为新的爬取调用的parse名称，这个项目新定义的为parse_item。
            yield response.follow(href[0], callback=self.parse_dogattributeint)

    def parse_dogattributeint(self,response):
        href = response.xpath('//div[@id="car_tag"]/ul/li/a/@href').extract()
        #print(href)
        yield response.follow(href[1], callback=self.parse_doginfo)



    #详细信息界面
    def parse_doginfo(self,response):
        valist = self.getBaseInfo(response.xpath('//div[@class="Details_main"]/ul'))
        valist2 = self.getCompleteInfo(response.xpath('//div[@class="Details_content"]/div[@class="option_box"]/pre/p'))
        valist.extend(valist2)
        item = IpetsItem()
        item['reslist'] = valist
        yield item
        pass




    #狗的基本信息介绍
    def getBaseInfo(self,sel):
        for s in sel:
            val = s.xpath('li/text()').re(r'[\u4e00-\u9fa5_a-zA-Z0-9\.,，。：、]+')
        return val


    #完整的宠物狗介绍信息
    def getCompleteInfo(self,sel):
        val = []
        for s in sel:
            tempres = s.xpath('.//span//text()').re(r'[\u4e00-\u9fa5_a-zA-Z0-9\.,，。：、]+')
            print(tempres)
            val.extend(tempres)
        return val

