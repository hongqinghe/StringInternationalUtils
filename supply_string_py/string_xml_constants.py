# string 共用参数
#!/usr/bin/env python3
# -*- coding: utf-8 -*-


baseUri = '/Users/hehongqing/WorkSpace/utilsMaven/GYLStringModule'
_supplybase_zh_btns_path =baseUri+'/SupplyBaseString/src/main/res/values/btns.xml'
_supplybase_en_btns_path = baseUri+'/SupplyBaseString/src/main/res/values-en/btns.xml'
_supplybase_thai_btns_path= baseUri+'/SupplyBaseString/src/main/res/values-th-rTH/btns.xml'

#  Base_btns_file 
_supplybase_zh_pages_path=baseUri+'/SupplyBaseString/src/main/res/values/pages.xml'
_supplybase_en_pages_path=baseUri+'/SupplyBaseString/src/main/res/values-en/pages.xml'
_supplybase_thai_pages_path = baseUri + \
    '/SupplyBaseString/src/main/res/values-th-rTH/pages.xml'

#  Base_btns_file 
_supplybase_zh_msgs_path=baseUri+'/SupplyBaseString/src/main/res/values/msgs.xml'
_supplybase_en_msgs_path=baseUri+'/SupplyBaseString/src/main/res/values-en/msgs.xml'
_supplybase_thai_msgs_path = baseUri + \
    '/SupplyBaseString/src/main/res/values-th-rTH/msgs.xml'


#  Base_btns_file 
_base_zh_btns_path=baseUri+'/BaseString/src/main/res/values/btns.xml'
_base_en_btns_path=baseUri+'/BaseString/src/main/res/values-en/btns.xml'
_base_thai_btns_path = baseUri+'/BaseString/src/main/res/values-th-rTH/btns.xml'

#  Base_pages_file compare 
_base_zh_pages_path=baseUri+'/BaseString/src/main/res/values/pages.xml'
_base_en_pages_path=baseUri+'/BaseString/src/main/res/values-en/pages.xml'
_base_thai_pages_path = baseUri+'/BaseString/src/main/res/values-th-rTH/pages.xml'


#  Base_msgs_file compare 
_base_zh_msgs_path=baseUri+'/BaseString/src/main/res/values/msgs.xml'
_base_en_msgs_path=baseUri+'/BaseString/src/main/res/values-en/msgs.xml'
_base_thai_msgs_path = baseUri+'/BaseString/src/main/res/values-th-rTH/msgs.xml'


#  buy_btns_file compare 
_buy_zh_btns_path=baseUri+'/PurchaseBuyString/src/main/res/values/btns.xml'
_buy_en_btns_path=baseUri+'/PurchaseBuyString/src/main/res/values-en/btns.xml'
_buy_thai_btns_path = baseUri+'/PurchaseBuyString/src/main/res/values-th-rTH/btns.xml'

#  buy_pages_file compare 
_buy_zh_pages_path=baseUri+'/PurchaseBuyString/src/main/res/values/pages.xml'
_buy_en_pages_path=baseUri+'/PurchaseBuyString/src/main/res/values-en/pages.xml'
_buy_thai_pages_path = baseUri + \
    '/PurchaseBuyString/src/main/res/values-th-rTH/pages.xml'


#  buy_msgs_file compare 
_buy_zh_msgs_path = baseUri+'/PurchaseBuyString/src/main/res/values/msgs.xml'
_buy_en_msgs_path = baseUri+'/PurchaseBuyString/src/main/res/values-en/msgs.xml'
_buy_thai_msgs_path = baseUri+'/PurchaseBuyString/src/main/res/values-th-rTH/msgs.xml'


# 每个string 对应的 sheet表头 
_excel_title_value_key='Key'
_excel_title_value_value='Value'
_excel_title_value_en='En'
_excel_title_value_thai='Thai'


# sheet name
_supply_base_sheet_head_btn='supply_base_btns'
_supply_base_sheet_head_page='supply_base_pages'
_supply_base_sheet_head_msg='supply_base_msgs'

_base_sheet_head_btn='base_btns'
_base_sheet_head_page='base_pages'
_base_sheet_head_msg='base_msgs'

_buy_sheet_head_btn='buy_btns'
_buy_sheet_head_page='buy_pages'
_buy_sheet_head_msg='buy_msgs'


# 文件路径
_supplyBaseBasicPath = baseUri+'/SupplyBaseString/src/main/res'
_baseBasicPath = baseUri+'/BaseString/src/main/res'
_buyBasicPath = baseUri+'/PurchaseBuyString/src/main/res'

_basicPathList = [_supplyBaseBasicPath, _baseBasicPath, _buyBasicPath]
# 文件名类型()
_basicTypeZH = '/values'
_basicTypeEN = '/values-en'
_basicTypeThai = '/values-th-rTH'
_basicTypeTW = '/values-zh-rTW'

# 语言列表 这里必须将zh位于第一个，方便后面进行检查设置
_basicTypeList = [_basicTypeZH, _basicTypeEN, _basicTypeTW]

# 文件后缀名 
_sourceSuffixBtn='/btns.xml'
_sourceSuffixPage='/pages.xml'
_sourceSuffixMsg='/msgs.xml'

_sourceSuffixList = [_sourceSuffixBtn, _sourceSuffixPage, _sourceSuffixMsg]

# 用于操作string 的辅助文件
_su_string_file_path = r'/Users/hehongqing/WorkSpace/utilsMaven/StringFileHelp/new_string_add.xml'
_base_maven_test_version = r'/Users/hehongqing/WorkSpace/utilsMaven/StringFileHelp/base_maven_test'
