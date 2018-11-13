#  xml  文件转化为 excel 文件

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
from openpyxl.workbook import Workbook
# 颜色
from openpyxl.styles import  PatternFill
from openpyxl.styles import Color, Fill
from openpyxl.cell import Cell
import string_xml_constants as SC
# # 每个sheet表头 
# _excel_title_value_key='Key'
# _excel_title_value_value='Value'
# _excel_title_value_en='En'
# _excel_title_value_thai='Thai'


# # sheet name
# _supply_base_sheet_head_btn='supply_base_btns'
# _supply_base_sheet_head_page='supply_base_pages'
# _supply_base_sheet_head_msg='supply_base_msgs'

# _base_sheet_head_btn='base_btns'
# _base_sheet_head_page='base_pages'
# _base_sheet_head_msg='base_msgs'

# _buy_sheet_head_btn='buy_btns'
# _buy_sheet_head_page='buy_pages'
# _buy_sheet_head_msg='buy_msgs'



def getSheetWs(wb,sheet_title):
    if SC._supply_base_sheet_head_btn==sheet_title:
        ws = wb.worksheets[0]
        ws.title = sheet_title
    else:
        ws = wb.create_sheet(sheet_title)
    ws.append({1: SC._excel_title_value_key, 2:SC._excel_title_value_value, 3: SC._excel_title_value_en, 4: SC._excel_title_value_thai})
    return ws
# def supplyBaseMsg(wb):
#     ws = wb.create_sheet('supply_base_msgs')
#     ws.append({1: 'Key', 2: 'Value', 3: 'En', 4: 'Thai'})
#     return ws

def initExcel(path):
    wb = Workbook()
    fileName = path
    # 开始写入 excel
    return  wb, fileName
 
# ws= getOnlyWs(TYPE_SUPPLY_BASE_BTNS)
def xmlParse(zhPath, enPath,ws):
    zh_tree = ET.parse(zhPath)
    en_tree = ET.parse(enPath)

    # 中文 xml  解析 生成对应的 key 和 value 
    for zh_elem in zh_tree.iter(tag='string'):
        zh_key = zh_elem.attrib['name']
        print('zh_key:      ' + str(zh_key))
        zh_value = zh_elem.text
        print('zh_value:    ' + str(zh_value))

        # 获取 key 对应的 en_value
        en_value=''
        for en_elem in en_tree.iter(tag='string'):
            en_key = en_elem.attrib['name']
            if en_key == zh_key:
                en_value = en_elem.text
                break
        #  添加字符串到excel中
        ws.append([zh_key, zh_value, en_value])

#  Base_btns_file 
# supplybase_zh_btns_path = '/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values/btns.xml'
# supplybase_en_btns_path = '/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values-en/btns.xml'

# #  Base_btns_file 
# supplybase_zh_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values/pages.xml'
# supplybase_en_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values-en/pages.xml'

# #  Base_btns_file 
# supplybase_zh_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values/msgs.xml'
# supplybase_en_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values-en/msgs.xml'


# #  Base_btns_file 
# base_zh_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values/btns.xml'
# base_en_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values-en/btns.xml'

# #  Base_pages_file compare 
# base_zh_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values/pages.xml'
# base_en_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values-en/pages.xml'


# #  Base_msgs_file compare 
# base_zh_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values/msgs.xml'
# base_en_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values-en/msgs.xml'


# #  buy_btns_file compare 
# buy_zh_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values/btns.xml'
# buy_en_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values-en/btns.xml'

# #  buy_pages_file compare 
# buy_zh_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values/pages.xml'
# buy_en_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values-en/pages.xml'


# #  buy_msgs_file compare 
# buy_zh_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values/msgs.xml'
# buy_en_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values-en/msgs.xml'

su_string_file_path=r'/Users/hehongqing/Downloads/supply_string_2.xlsx'

def transformToExcel():

    # 初始化excel 的必要参数
    wb, fileName = initExcel(su_string_file_path)

    # supplyBase
    xmlParse(SC._supplybase_zh_btns_path,SC._supplybase_en_btns_path,getSheetWs(wb,SC._supply_base_sheet_head_btn))
    xmlParse(SC._supplybase_zh_pages_path,SC._supplybase_en_pages_path,getSheetWs(wb,SC._supply_base_sheet_head_page))
    xmlParse(SC._supplybase_zh_msgs_path,SC._supplybase_en_msgs_path,getSheetWs(wb,SC._supply_base_sheet_head_msg))

    # base
    xmlParse(SC._base_zh_btns_path,SC._base_en_btns_path,getSheetWs(wb,SC._base_sheet_head_btn))
    xmlParse(SC._base_zh_pages_path,SC._base_en_pages_path,getSheetWs(wb,SC._base_sheet_head_page))
    xmlParse(SC._base_zh_msgs_path,SC._base_en_msgs_path,getSheetWs(wb,SC._base_sheet_head_msg))

    # Buy
    xmlParse(SC._buy_zh_btns_path,SC._buy_en_btns_path,getSheetWs(wb,SC._buy_sheet_head_btn))
    xmlParse(SC._buy_zh_pages_path,SC._buy_en_pages_path,getSheetWs(wb,SC._buy_sheet_head_page))
    xmlParse(SC._buy_zh_msgs_path,SC._buy_en_msgs_path,getSheetWs(wb,SC._buy_sheet_head_msg))

    # 在每个 ws 对象添加节点后对文件做保存操作，不然不会生效
    wb.save(fileName)
if __name__ == "__main__":
    transformToExcel()
