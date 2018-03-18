import csv

"""
把爬取的数据保存到cvs
"""
class CSVPipeline(object):

  def process_item(self, item, ampa):
    with open('E:/items.csv', 'a', encoding='gbk',newline='') as f:# 设置newline，否则两行之间会空一行
      csvwriter = csv.writer(f)
      csvwriter.writerow(item['reslist'])#必须传入list类型的数据  不然自动转类型过程中 输出的数据会有问题 例如传入的是字符串 百度以下 转list  变成 百，度，一，下

    return item