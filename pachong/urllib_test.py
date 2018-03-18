"""
它包含四个模块：
第一个模块 request，它是最基本的 HTTP 请求模块，我们可以用它来模拟发送一请求，就像在浏览器里输入网址然后敲击回车一样，
只需要给库方法传入 URL 还有额外的参数，就可以模拟实现这个过程了。
第二个 error 模块即异常处理模块，如果出现请求错误，我们可以捕获这些异常，然后进行重试或其他操作保证程序不会意外终止。
第三个 parse 模块是一个工具模块，提供了许多 URL 处理方法，比如拆分、解析、合并等等的方法。
第四个模块是 robotparser，主要是用来识别网站的 robots.txt 文件，然后判断哪些网站可以爬，哪些网站不可以爬的，其实用的比较少。
"""

import urllib.request
import urllib.parse

def test1():
    response = urllib.request.urlopen('http://www.baidu.com')
    #返回的response是urllib.request.HTTPResposne对象；
    # 它主要包含的方法有 read()、readinto()、getheader(name)、getheaders()、fileno() 等方法和 msg、version、status、reason、debuglevel、closed 等属性。
    print(response)
    assert isinstance(response, urllib.request.HTTPResposne)
    b = response.read()
    s = b.decode('utf-8')
    print(type(b))


#设置data参数，传递参数,data需要是一个字节类型的数据
def test2():
    data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')#urlencode作用是将字典数据转字符串数据
    response = urllib.request.urlopen('http://www.baidu.com',data=data)
    print(response.read().decode('utf-8'))


#timeout参数的使用,设置时间，如果在设置的时间内 没有得到响应 就抛出异常
def test3():
    try:
        response = urllib.request.urlopen('http://www.baidu.com',timeout=0.0000001)
        print(response.read().decode('utf-8'))
    except:
        pass



test3()
