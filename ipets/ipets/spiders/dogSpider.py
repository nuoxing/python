import scrapy

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



    def parse_doginfo(self,response):
        #print(response.body)
        name = response.xpath('//div[@class="pet_nav_top"]/h2/text()').extract()
        plist = response.xpath('//div[@class="Details_content"]/div[@class="option_box"]/pre/p')
        introduce = plist[0].xpath('span/span/text()').extract()


