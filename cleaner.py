# -*- coding: UTF-8 -*-
import pandas as pd
import xlrd
import re

fileName = '编码20150228最终版(查).xlsx'
df = pd.read_excel(fileName)

class Cleaner:
    def clean(self):
        spec = '规格型号'

        for idx,row in df.iterrows():
            cell = df.loc[idx,spec] #str object
            #去除首尾空格
            df.set_value(idx,spec,cell.strip())
            #去除中间空格
            if ' ' in cell:
                df.set_value(idx,spec,''.join(cell.split()))
            # 小写字母装换
            if (re.search(r'.*[a-z].*',cell) != None):
                #去除包含单位
                if(re.match(r'^((?!kW).)*$', cell) != None) and (re.match(r'^((?!kΩ).)*$', cell) != None):
                        df.set_value(idx,spec,cell.upper())
            # 替换包含错误下划线模式
            if (re.search(r'[_]',cell) != None):
                df.set_value(idx,spec,cell.replace('_', '-'))
            if (re.search(r'[－]',cell) != None):
                df.set_value(idx,spec,cell.replace('－', '-'))

        #检查包含全角数字字母dash
        for idx,row in df.iterrows():
            cell = df.loc[idx,spec] #str object
            if (re.search(r'[^0-9a-zA-Z-]',cell) != None):
                print(cell)
                mis = cell

        print(' ' in mis.strip())

        print(df)

        #写入excel
        df.to_excel('excel_output.xlsx')

        #regex测试
        eg = " 2000W"
        # eg = " SCREEN"
        #去除首尾空格
        # if ' ' in eg:
        #     eg = eg.strip()
        # print(eg)

        #去除中间空格
        # eg = ''.join(eg.split())
        # print(eg)
        # print(re.match(r'[0-9]*', eg) == True)

        #包含小写字母
        # print(re.match(r'.*[a-z].*',eg))

        #包含特定字符
        # print(re.match(r'^((?!kW).)*$',eg))

        #检查包含半角数组符号
        # print(re.search(r'[^0-9a-zA-Z]+',eg))

c = Cleaner()
c.clean()
