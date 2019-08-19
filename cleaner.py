# -*- coding: UTF-8 -*-
import pandas as pd
import xlrd

class Cleaner:
    # def __init__(self):
    #     self.sql_engine = create_engine("mysql+mysqlconnector://root:@127.0.0.1:3306/drug?ssl_disabled='True", echo=False)
    #     self.conn = mysql.connector.connect(user='root', password='mysql123', database='drug', use_unicode=True, auth_plugin='mysql_native_password')
    #     self.cursor = self.conn.cursor()


    def __init__(self):
        self.file = '编码20150228最终版(查).xlsx'

    def readXls(self):
        df = pd.read_excel(self.file)
        np_df = df.as_matrix()
        print(np_df)
        print(unicode(np_df, encoding="utf-8"))

    # def saveDrug(self):
    #     df = yzc.getItems()
    #     np_df = df.as_matrix()
    #     print(np_df)
    #     for row in np_df:
    #         self.cursor.execute('insert into drugInfo(drugSubgroup, drugName, indication) values(%s,%s,%s)',
    #                             [row[0], row[1], row[2]])
    #     self.conn.commit()

c = Cleaner()
c.readXls()
