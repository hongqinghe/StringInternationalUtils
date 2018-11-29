# en_xml文件的key是不是在zh_xml

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree

import threading
import time

def xmlParse(old_zh_path,old_en_path):
    old_zh_tree= ET.parse(old_zh_path)

    old_en_tree= ET.parse(old_en_path)

    old_zh_root=old_zh_tree.getroot()
    old_en_root=old_en_tree.getroot()

    # root.tag 由于root  是element对象 使用tag取得tag
    # 生成新的xml文件的 xml 属性获取 
    xmlroot=Element(old_zh_root.tag)
    xmltree=ElementTree(xmlroot)

     # 生成 en list
    zh_list_key=[]

    for zh_elem in  old_zh_tree.iter(tag='string'):
            zh_key=zh_elem.attrib['name']
            zh_list_key.append(zh_key)
    for en_elem in  old_en_tree.iter(tag='string'):
        en_key= en_elem.attrib['name']
        if  not en_key in zh_list_key:
            print(en_key)
#  supplyBase_btns_file compare
old_supplybase_ch_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values/btns.xml'
old_supplybase_en_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values-en/btns.xml'
no_trans_supplybase_btns_path='/Users/hehongqing/WorkSpace/stringCompareFile/supplyBase/btns.xml'

#  supplyBase_pages_file compare  
old_supplybase_ch_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values/pages.xml'
old_supplybase_en_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values-en/pages.xml'
no_trans_supplybase_pages_path='/Users/hehongqing/WorkSpace/stringCompareFile/supplyBase/pages.xml'




#  supplyBase_msg_file compare  
old_supplybase_ch_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values/msgs.xml'
old_supplybase_en_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values-en/msgs.xml'
no_trans_supplybase_msgs_path='/Users/hehongqing/WorkSpace/stringCompareFile/supplyBase/msgs.xml'



#  Base_btns_file compare 
old_base_ch_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values/btns.xml'
old_base_en_bnts_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values-en/btns.xml'
no_trans_base_btns_path='/Users/hehongqing/WorkSpace/stringCompareFile/base/btns.xml'


#  Base_pages_file compare 
old_base_ch_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values/pages.xml'
old_base_en_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values-en/pages.xml'
no_trans_base_pages_path='/Users/hehongqing/WorkSpace/stringCompareFile/base/pages.xml'


#  Base_msgs_file compare 
old_base_ch_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values/msgs.xml'
old_base_en_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values-en/msgs.xml'
no_trans_base_msgs_path='/Users/hehongqing/WorkSpace/stringCompareFile/base/msgs.xml'


#  buy_btns_file compare 
old_buy_ch_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values/btns.xml'
old_buy_en_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values-en/btns.xml'
no_trans_buy_btns_path='/Users/hehongqing/WorkSpace/stringCompareFile/buy/btns.xml'



#  buy_pages_file compare 
old_buy_ch_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values/pages.xml'
old_buy_en_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values-en/pages.xml'
no_trans_buy_pages_path='/Users/hehongqing/WorkSpace/stringCompareFile/buy/pages.xml'



#  buy_msgs_file compare 
old_buy_ch_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values/msgs.xml'
old_buy_en_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values-en/msgs.xml'
no_trans_buy_msgs_path='/Users/hehongqing/WorkSpace/stringCompareFile/buy/msgs.xml'

xmlParse(old_base_ch_msgs_path,old_base_en_msgs_path)
xmlParse(old_base_ch_btns_path,old_base_en_bnts_path)
xmlParse(old_base_ch_pages_path,old_base_en_pages_path)

xmlParse(old_supplybase_ch_msgs_path,old_supplybase_en_msgs_path)
xmlParse(old_supplybase_ch_btns_path,old_supplybase_en_btns_path)
xmlParse(old_supplybase_ch_pages_path,old_supplybase_en_pages_path)

xmlParse(old_buy_ch_msgs_path,old_buy_ch_msgs_path)
xmlParse(old_buy_ch_btns_path,old_buy_ch_btns_path)
xmlParse(old_buy_ch_pages_path,old_buy_ch_pages_path)

