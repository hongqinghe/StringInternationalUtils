#  xml  文件转化为 excel 文件
import re
import os

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
from openpyxl.workbook import Workbook
# 颜色
from openpyxl.styles import  PatternFill
from openpyxl.styles import Color, Fill
from openpyxl.cell import Cell


TYPE_SUPPLY_BASE_BTNS = 1
TYPE_SUPPLY_BASE_PAGES = 2
TYPE_SUPPLY_BASE_MSGS = 3

TYPE_BASE_BTNS = 4
TYPE_BASE_PAGES = 5
TYPE_BASE_MSGS = 6

TYPE_BUY_BTNS = 7
TYPE_BUY_PAGES = 8
TYPE_BUY_MSGS = 9

# def supplyBaseBtn(wb):
#     ws = wb.worksheets[0]
#     ws.title = 'supply_base_btns'
#     ws.append({1: 'Key', 2: 'Value', 3: 'En', 4: 'Thai'})
#     return ws

# 
def getSheetWs(wb,sheet_title):
    if SUPPLY_BASE_SHEET_TITLE_BTN==sheet_title:
        ws = wb.worksheets[0]
        ws.title = sheet_title
    else:
        ws = wb.create_sheet(sheet_title)
    ws.append({1: 'Key', 2: 'Value', 3: 'En', 4: 'Thai'})
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
supplybase_zh_btns_path = '/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values/btns.xml'
supplybase_en_btns_path = '/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values-en/btns.xml'

#  Base_btns_file 
supplybase_zh_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values/pages.xml'
supplybase_en_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values-en/pages.xml'

#  Base_btns_file 
supplybase_zh_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values/msgs.xml'
supplybase_en_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values-en/msgs.xml'


#  Base_btns_file 
base_zh_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values/btns.xml'
base_en_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values-en/btns.xml'

#  Base_pages_file compare 
base_zh_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values/pages.xml'
base_en_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values-en/pages.xml'


#  Base_msgs_file compare 
base_zh_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values/msgs.xml'
base_en_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values-en/msgs.xml'




#  buy_btns_file compare 
buy_zh_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values/btns.xml'
buy_en_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values-en/btns.xml'

#  buy_pages_file compare 
buy_zh_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values/pages.xml'
buy_en_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values-en/pages.xml'


#  buy_msgs_file compare 
buy_zh_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values/msgs.xml'
buy_en_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values-en/msgs.xml'

su_string_file_path=r'/Users/hehongqing/Downloads/supply_string.xlsx'

SUPPLY_BASE_SHEET_TITLE_BTN='supply_base_btns'
SUPPLY_BASE_SHEET_TITLE_PAGE='supply_base_pages'
SUPPLY_BASE_SHEET_TITLE_MSG='supply_base_msgs'

BASE_SHEET_TITLE_BTN='base_btns'
BASE_SHEET_TITLE_PAGE='base_pages'
BASE_SHEET_TITLE_MSG='base_msgs'

BUY_SHEET_TITLE_BTN='buy_btns'
BUY_SHEET_TITLE_PAGE='buy_pages'
BUY_SHEET_TITLE_MSG='buy_msgs'

def transformToExcel():

    # 初始化excel 的必要参数
    wb, fileName = initExcel(su_string_file_path)

    # supplyBase
    xmlParse(supplybase_zh_btns_path,supplybase_en_btns_path,getSheetWs(wb,SUPPLY_BASE_SHEET_TITLE_BTN))
    xmlParse(supplybase_zh_pages_path,supplybase_en_pages_path,getSheetWs(wb,SUPPLY_BASE_SHEET_TITLE_PAGE))
    xmlParse(supplybase_zh_msgs_path,supplybase_en_msgs_path,getSheetWs(wb,SUPPLY_BASE_SHEET_TITLE_MSG))

    # base
    xmlParse(base_zh_btns_path,base_en_btns_path,getSheetWs(wb,BASE_SHEET_TITLE_BTN))
    xmlParse(base_zh_pages_path,base_en_pages_path,getSheetWs(wb,BASE_SHEET_TITLE_PAGE))
    xmlParse(base_zh_msgs_path,base_en_msgs_path,getSheetWs(wb,BASE_SHEET_TITLE_MSG))

    # Buy
    xmlParse(buy_zh_btns_path,buy_en_btns_path,getSheetWs(wb,BUY_SHEET_TITLE_BTN))
    xmlParse(buy_zh_pages_path,buy_en_pages_path,getSheetWs(wb,BUY_SHEET_TITLE_PAGE))
    xmlParse(buy_zh_msgs_path,buy_en_msgs_path,getSheetWs(wb,BUY_SHEET_TITLE_MSG))

    # 在每个 ws 对象添加节点后对文件做保存操作，不然不会生效
    wb.save(fileName)
# 入口函数
transformToExcel()

