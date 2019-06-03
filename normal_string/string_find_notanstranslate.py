# 查找string 库中未翻译的文件

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree

import threading
import time
def xmlParse(old_ch_path,old_en_path,input_no_trans_path):
    old_ch_tree= ET.parse(old_ch_path)
    old_en_tree= ET.parse(old_en_path)

    old_ch_root=old_ch_tree.getroot()
    old_en_root=old_en_tree.getroot()

    # root.tag 由于root  是element对象 使用tag取得tag
    # 生成新的xml文件的 xml 属性获取 
    xmlroot=Element(old_ch_root.tag)
    xmltree=ElementTree(xmlroot)

    print(old_ch_root)
     # 生成 en list
    now_en_list=[]
    for en_elem in  old_en_tree.iter(tag='string'):
        en_stirngId=en_elem.attrib
        now_en_list.append(en_stirngId)
    for ch_elem in old_ch_tree.iter(tag='string'):        
        ch_stringId=(ch_elem.attrib)
        stringValue=(ch_elem.attrib)['name']
        #  查出 ch_id 在 now_en_list 是否含有
        if ch_stringId not in now_en_list:
            xmlroot.append(ch_elem)
            xmltree.write(input_no_trans_path,encoding='utf-8',xml_declaration=True)

#  删除指定文件,目的是确保每次都生成最新的文件，没有差异的话就不会生成差异化文件
def removeXmlFile(tagetPath):
    if os.path.exists(tagetPath):
        os.remove(tagetPath)

#  supplyBase_btns_file compare
old_supplybase_ch_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values/btns.xml'
old_supplybase_en_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values-en/btns.xml'
no_trans_supplybase_btns_path='/Users/hehongqing/WorkSpace/stringCompareFile/supplyBase/btns.xml'

removeXmlFile(no_trans_supplybase_btns_path)
xmlParse(old_supplybase_ch_btns_path,old_supplybase_en_btns_path,no_trans_supplybase_btns_path)

#  supplyBase_pages_file compare  
old_supplybase_ch_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values/pages.xml'
old_supplybase_en_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values-en/pages.xml'
no_trans_supplybase_pages_path='/Users/hehongqing/WorkSpace/stringCompareFile/supplyBase/pages.xml'

removeXmlFile(no_trans_supplybase_pages_path)
xmlParse(old_supplybase_ch_pages_path,old_supplybase_en_pages_path,no_trans_supplybase_pages_path)

#  supplyBase_msg_file compare  
old_supplybase_ch_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values/msgs.xml'
old_supplybase_en_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/SupplyBaseString/src/main/res/values-en/msgs.xml'
no_trans_supplybase_msgs_path='/Users/hehongqing/WorkSpace/stringCompareFile/supplyBase/msgs.xml'

removeXmlFile(no_trans_supplybase_msgs_path)
xmlParse(old_supplybase_ch_msgs_path,old_supplybase_en_msgs_path,no_trans_supplybase_msgs_path)


#  Base_btns_file compare 
old_base_ch_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values/btns.xml'
old_base_en_bnts_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values-en/btns.xml'
no_trans_base_btns_path='/Users/hehongqing/WorkSpace/stringCompareFile/base/btns.xml'

removeXmlFile(no_trans_base_btns_path)
xmlParse(old_base_ch_btns_path,old_base_en_bnts_path,no_trans_base_btns_path)

#  Base_pages_file compare 
old_base_ch_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values/pages.xml'
old_base_en_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values-en/pages.xml'
no_trans_base_pages_path='/Users/hehongqing/WorkSpace/stringCompareFile/base/pages.xml'

removeXmlFile(no_trans_base_pages_path)
xmlParse(old_base_ch_pages_path,old_base_en_pages_path,no_trans_base_pages_path)

#  Base_msgs_file compare 
old_base_ch_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values/msgs.xml'
old_base_en_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/BaseString/src/main/res/values-en/msgs.xml'
no_trans_base_msgs_path='/Users/hehongqing/WorkSpace/stringCompareFile/base/msgs.xml'

removeXmlFile(no_trans_base_msgs_path)
xmlParse(old_base_ch_msgs_path,old_base_en_msgs_path,no_trans_base_msgs_path)



#  buy_btns_file compare 
old_buy_ch_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values/btns.xml'
old_buy_en_btns_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values-en/btns.xml'
no_trans_buy_btns_path='/Users/hehongqing/WorkSpace/stringCompareFile/buy/btns.xml'

removeXmlFile(no_trans_buy_btns_path)
xmlParse(old_buy_ch_btns_path,old_buy_en_btns_path,no_trans_buy_btns_path)

#  buy_pages_file compare 
old_buy_ch_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values/pages.xml'
old_buy_en_pages_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values-en/pages.xml'
no_trans_buy_pages_path='/Users/hehongqing/WorkSpace/stringCompareFile/buy/pages.xml'

removeXmlFile(no_trans_buy_pages_path)
xmlParse(old_buy_ch_pages_path,old_buy_en_pages_path,no_trans_buy_pages_path)

#  buy_msgs_file compare 
old_buy_ch_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values/msgs.xml'
old_buy_en_msgs_path='/Users/hehongqing/WorkSpace/Android/GYLStringModule/PurchaseBuyString/src/main/res/values-en/msgs.xml'
no_trans_buy_msgs_path='/Users/hehongqing/WorkSpace/stringCompareFile/buy/msgs.xml'

removeXmlFile(no_trans_buy_msgs_path)
xmlParse(old_buy_ch_msgs_path,old_buy_en_msgs_path,no_trans_buy_msgs_path)
