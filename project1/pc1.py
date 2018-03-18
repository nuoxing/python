#!/usr/bin/python
#python 3.5爬虫例子，需要使用urllib.request
import urllib.request

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.63 Safari/537.36'}
#请求
req = urllib.request.Request(url="http://www.baidu.com",headers=headers)
#获取结果
response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
f = open("E:/a.txt",'w',encoding="utf-8") #open函数返回一个file对象 第一个参数是文件路路径 第二个参数是打开文件的选项 第三个参数是输出数据的编码
f.write(data)
f.close()