# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: interfaceTest
# author: "Lei Yong" 
# creation time: 2018/3/19 0019 22:50
# Email: leiyong711@163.com
import xlrd


def geteExcel(fname):
    bk = xlrd.open_workbook(fname)
    try:
        sh = bk.sheet_by_name('Sheet1')
    except:
        print("%没有表名为Sheet1的" % fname)
    # 获取行数
    nrows = sh.nrows
    # 获取列数
    ncols = sh.ncols
    print("用例数：%s 行 %s 列" % (nrows,ncols))
    a = []
    for i in range(0, nrows):
        c = sh.row_values(i)
        # if i == 0:
        #     continue
        # else:
        #     c[0] = int(c[0])
        #     c[6] = int(c[6])
        a.append(c)
    return a


if __name__ == "__main__":
    print(geteExcel("..\\case\\test.xlsx"))

