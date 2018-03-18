#!/usr/bin/python

import keyword
print("hello world")
print(keyword.kwlist)
print("1");print("b")
print("a",end="")#以end=""结束可以不换行
print("a")

a,b,c,d = 20,5.5,True,4+3j
print(type(a),type(b))

list = ['aa','1']

dic = {"a":"ce","a":"v"}
print(dic["a"])

print(list * 2)



a=10
b=20
while a < b:
    print(a)
    a+=1;
    if a==12:
        break
else:
    print("else")