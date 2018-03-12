from scrapy import cmdline
import re
"""
启动scrapy的命令入口
"""

cmdline.execute("scrapy crawl dog".split())
s = re.sub('\s',"","fdf fdfd")
print(s)