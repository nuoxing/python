from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from scrapy.http import HtmlResponse
"""
scrapy的下载器中间件 位置在scrapy引擎与download之间 
"""

class PhantomJSMiddleware(object):
    @classmethod
    def process_request(cls, request, spider):
        print('========================调用==================')
        driver = webdriver.Chrome()
        driver.get(request.url)
        content = driver.page_source.encode('utf-8')
        driver.quit()
        return HtmlResponse(request.url, encoding='utf-8', body=content, request=request)