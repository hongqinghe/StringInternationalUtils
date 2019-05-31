#  基本文件为zh_xml文件，如果其他文件中多出zh_xml节点，则打印，手动根据需求进行设置

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree

import threading
import time
import string_xml_constants as SC


def xmlParse(old_zh_path, old_en_path):
    old_zh_tree = ET.parse(old_zh_path)

    old_en_tree = ET.parse(old_en_path)

    # 生成新的xml文件的 xml 属性获取
    # 生成 en list
    zh_list_key = []

    for zh_elem in old_zh_tree.iter(tag='string'):
        zh_key = zh_elem.attrib['name']
        zh_list_key.append(zh_key)
    for en_elem in old_en_tree.iter(tag='string'):
        en_key = en_elem.attrib['name']
        if not en_key in zh_list_key:
            print(en_key)


# 根据basicpath  语言种类 字符串分类 分别对应出最终的resouce path，进行check[是否其他文件中id不在中文xml中，如果不在进行删除]，基类版本永远是zh_xml
def pathTransformAndToCheck():
    # 注意这里容易产生误差数据为0
    try:
        zhPath = SC._basicTypeList[0]
        tempList = SC._basicTypeList
        tempList.remove(zhPath)
        print('\n#########check进行中，不在中文xml文件中的id 如下：##################\n')
        for basicPath in SC._basicPathList:
            for index in range(len(tempList)):
                # print(tempList[index])
                for sourceSuffix in SC._sourceSuffixList:
                    xmlParse(basicPath + zhPath + sourceSuffix,
                             basicPath + tempList[index] + sourceSuffix)
        print('\n#########file 多出ID check完毕，请注意以上结果\n')
    except  Exception:
        print('数据发生异常，请检查数据是否为空【SC._basicTypeList】')


# 检测文件中是否含有多个重复的Id定义
# def haveMultipleID():

if __name__ == "__main__":
    pathTransformAndToCheck()

# xmlParse(SC._base_zh_msgs_path,SC._base_en_msgs_path)
# xmlParse(SC._base_zh_btns_path,SC._base_en_btns_path)
# xmlParse(SC._base_zh_pages_path,SC._base_en_pages_path)

# xmlParse(SC._supplybase_zh_msgs_path,SC._supplybase_en_msgs_path)
# xmlParse(SC._supplybase_zh_btns_path,SC._supplybase_en_btns_path)
# xmlParse(SC._supplybase_zh_pages_path,SC._supplybase_en_pages_path)

# xmlParse(SC._buy_zh_msgs_path,SC._buy_en_msgs_path)
# xmlParse(SC._buy_zh_btns_path,SC._buy_en_btns_path)
# xmlParse(SC._buy_zh_pages_path,SC._buy_en_pages_path)
