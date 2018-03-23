# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: interfaceTest1
# author: "Lei Yong" 
# creation time: 2018/3/23 0023 21:58
# Email: leiyong711@163.com

import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from readCase.getCase import *


def getQuest(case):

    if case[4].upper() == 'GET':
        data = case[3].replace(',', '&')
        url = case[2] + '?' + data
        print url
        req = urllib2.Request(url)
        html = urllib2.urlopen(req).read()
        print(html)

    elif case[4].upper() == 'POST':
        # print('post')
        url = case[2]
        jiequ = case[3].split(',')
        data = {}
        for i in range(len(jiequ)):
            spli = jiequ[i].split('=')
            data[spli[0]] = spli[1]
        print(data)
        req = urllib.urlencode(data)
        html = urllib2.urlopen(url, req).read()
        print(html)
    else:
        print("请求方式异常,请确保请求方式为GET/POST。。。")


if __name__ == "__main__":
    case = geteExcel("..\\case\\test.xlsx")
    for i in case:
        print i
        getQuest(i)
