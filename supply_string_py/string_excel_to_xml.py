#  xml  文件转化为 excel 文件
import re
import os

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
from openpyxl.workbook import Workbook
import  xlrd

def getExceltable(excelPath):
    #打开excel文件
    data=xlrd.open_workbook(path)     
    #获取第一张工作表（通过索引的方式）
    table=data.sheets()[0] 
    # 获取 sheet name
    sheetsNanme=table.name
    print('工作表名称'+sheetsNanme)
    return table
