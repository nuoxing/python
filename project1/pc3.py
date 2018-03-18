#!/usr/bin/python

import  re

f = open("E:/a.txt",'r',encoding="utf-8")
data = f.read()
list1 = re.findall(r'https:[^s]*?(jpg|png|gif)',data)
for s in list1:
    print(s)
    print(type(s))