import csv
import itertools
"""
把爬取的数据保存到cvs
"""
class CSVPipeline(object):
  def __init__(self):
    self.csvwriter = csv.writer(open('E:/items.csv', 'w', encoding='gbk',newline=''), dialect='excel')
    #self.csvwriter.writerow(['title'])

  def process_item(self, item, ampa):
    self.csvwriter.writerow(item['reslist'])#必须传入list类型的数据  不然自动转类型过程中 输出的数据会有问题 例如传入的是字符串 百度以下 转list  变成 百，度，一，下

    return item