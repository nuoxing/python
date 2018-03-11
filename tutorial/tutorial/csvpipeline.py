import csv
import itertools

class CSVPipeline(object):
  def __init__(self):
    self.csvwriter = csv.writer(open('E:/items.csv', 'w', encoding='gbk',newline=''), dialect='excel')
    self.csvwriter.writerow(['title'])

  def process_item(self, item, ampa):
    print(item['title'])
    self.csvwriter.writerow(['fdfhdfudfhdi'])

    return item