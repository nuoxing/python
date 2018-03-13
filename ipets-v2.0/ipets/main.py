from scrapy import cmdline
import re
"""
启动scrapy的命令入口
"""

cmdline.execute("scrapy crawl dog".split())
s = re.sub(r'\\xa0',"","fdffdfd\\xa0")
print(s)