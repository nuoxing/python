'''
批量下载豆瓣首页的图片

采用伪装浏览器的方式爬取豆瓣网站首页的图片，保存到指定路径文件夹下
'''

#导入所需的库
import urllib.request,re,os

#定义文件保存路径
targetPath = "E:\\projects\\a\\ab"

def saveFile(path):
    #检测当前路径的有效性 if not 判断是否None是None就执行
    #os.path.isdir()判断是否是目录名 存在是返回True 不是则Flase
    if not os.path.isdir(targetPath):
        os.makedirs(targetPath) #os.mkdir()不能创建多级目录  os.makedirs()可以创建多级目录

    #设置每个图片的路径
    pos = path.rindex('/')
    t = os.path.join(targetPath,path[pos+1:])
    return t

#用if __name__ == '__main__'来判断是否是在直接运行该.py文件


# 网址
url = "https://www.douban.com/"
headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '                            'Chrome/51.0.2704.63 Safari/537.36'
           }

req = urllib.request.Request(url=url, headers=headers)

res = urllib.request.urlopen(req)

# res.read()返回的是字节
data = res.read()

#re.findall正则表达式其中一个方法，返回的是所有匹配的子串 最外是list类型 list中类型根据正则表达式的括号 一个括号就是字符串 两个以上就是元组
#str()函数作用是将传入的对象转字符串
#set() 删除重复数据
#for in 遍历序列 因为遍历的是 元组类型的数据 使用两个变量接收可以分别把元组中的数据单独获取到
for link,t in set(re.findall(r'(https:[^s]*?(jpg|png|gif))', str(data))):
    print(link)
    try:
        urllib.request.urlretrieve(link,saveFile(link))
    except:
        print('失败')