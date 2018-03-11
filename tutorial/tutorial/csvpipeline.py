import csv
import itertools

class CSVPipeline(object):
  def __init__(self):
    self.csvwriter = csv.writer(open('E:/items.csv', 'w', encoding='gbk',newline=''), dialect='excel')
    self.csvwriter.writerow(['title'])

  def process_item(self, item, ampa):
    list1 = [];
    list1.append(item['title'])
    print(list1)
    self.csvwriter.writerow(list1)

    return item