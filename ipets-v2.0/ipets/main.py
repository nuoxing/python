from scrapy import cmdline
import re
"""
启动scrapy的命令入口
"""

cmdline.execute("scrapy crawl dog".split())
s = re.sub(r'\s',"","fdffdfd  a0")
print(s)