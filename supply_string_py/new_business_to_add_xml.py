# 业务中对字符串的操作（增删改查），用于业务string的迭代

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
import string_xml_constants as SC
import string_tw_zh_convert as ZW 

su_string_file_path = r'/Users/hehongqing/Downloads/new_string_add.xml'
attribName = 'name'
attribLocation = 'location'
attribStringType = 'stringType'
attribOperateType = 'operateType'

operateTypeAdd = 'A'
operateTypeUpdate = 'U'
operateTypeDelete = 'D'

locationSupplyBase = '0'
locationBaseModule = '1'
lcoationBuy = '2'

stringTypeBtns='A'
stringTypePages='B'
stringTypeMsgs='C'
def getFilePath(sourceType,path,stringType):
    if stringType == stringTypeBtns:
        path = path+sourceType+SC._sourceSuffixBtn
    if stringType==stringTypePages:
        path = path+sourceType+SC._sourceSuffixPage
    if stringType==stringTypeMsgs:
        path = path+sourceType+SC._sourceSuffixMsg
    return path

# 添加新的string到xml文件中，第一步添加string到中文xml中，第二步将中文xml转化为繁体
def addString(path,id,stringType,text):
    
    zhPath=getFilePath(SC._basicTypeZH,path,stringType)
    file = open(zhPath)
    lines = file.readlines()  # 读取所有行
    size = len(lines)
    xmlLine = '    <string name="'+id+'">'+text+'</string>\n'
    lines.insert(size-1, xmlLine)
    newFile = open(zhPath, 'w+')
    newFile.writelines(lines)
    newFile.close()

    # 添加完string之后同步进行繁体的转化
    twpath = getFilePath(SC._basicTypeTW, path, stringType)
    converList=ZW.fileConvertTraditional(zhPath)
    twFile = open(twpath, 'w+')
    twFile.writelines(converList)
    twFile.close


# 删除指定id的string,
def deleteString(path,id,stringType):
    typeList = SC._basicTypeList
    for type in typeList:
        newPath = getFilePath(type,path, stringType)
        xmlTree = ET.parse(newPath)
        xmlRoot=xmlTree.getroot()
        for xmlElem in xmlTree.iter(tag='string'):
            xmlId=xmlElem.attrib['name']
            if id==xmlId:
                xmlRoot.remove(xmlElem)
        xmlTree.write(newPath, encoding='utf-8', xml_declaration=True)

# 判断是那种操作类型 增加 删除  更新
def dealPathString(path, id, stringType, operateType, text):
    if operateType == operateTypeAdd:
        # add stirng to supplybase
        addString(path,id,stringType,text)

    elif operateType == operateTypeUpdate:
            # 打开文件删除指定的ID，并且key+1添加新字符
        deleteString(path, id, stringType)
        pattern = r'(?P<VERSION>\d)'
        # gyl_msg_shop_v1
        match=re.search(pattern,id)
        versionCode = match.group('VERSION')
        newVersion= int(versionCode)+1
        # 版本加一之后进行添加新的字符串
        id=id.replace(versionCode,str(newVersion))
        addString(path, id, stringType, text)
    elif operateType == operateTypeDelete:
            # 删除指定文件ID
        deleteString(path,id,stringType)
    else:
            # 文件类型错误
        raise RuntimeError('operatetype  error')

# 解析文件位置得出最前面的path
def dealWithString(id, location, stringType, operateType, text):
    if location == locationSupplyBase:
        dealPathString(SC._supplyBaseBasicPath, id,stringType, operateType, text)
    elif location == locationBaseModule:
        dealPathString(SC._baseBasicPath, id, stringType, operateType, text)
    elif location==lcoationBuy:
        dealPathString(SC._buyBasicPath, id, stringType, operateType, text)
    else:
        raise RuntimeError('location  error')

# 根据传入的文件路径解析需要新添加的字符串

# <root >
# 0 基础模块（SupplyBase） 1 公用模块(BaseModule) 2(采购平台)  supplyBase 和 BaseModule 的划分需要Android这边来负责
# <string name = "gyl_msg_menu_unit_default_v1" location = "0" stringType = 'A' operateType = "A" > 份 | 例 | 瓶 | 个 | 杯 </string >
# <string name = "gyl_msg_menu_unit_default_v1" location = "1" stringType = 'B' operateType = "U" > 更新键 </string >
# <string name = "gyl_msg_menu_unit_default_v1" location = "2" stringType = 'C' operateType = "D" > 删除键 </string >
# </root >

def xmlParse(path):
    xmlTree = ET.parse(path)
    for xmlElem in xmlTree.iter(tag='string'):
        stringId = xmlElem.attrib[attribName]
        stringLocation = xmlElem.attrib[attribLocation]
        stringType = xmlElem.attrib[attribStringType]
        stringOperateType = xmlElem.attrib[attribOperateType]
        stringValue = xmlElem.text
        dealWithString(stringId, stringLocation, stringType,
                       stringOperateType, stringValue)

def main(path):
    # 解析xml文件进行添加
    xmlParse(su_string_file_path)

if __name__ == "__main__":
    main(su_string_file_path)
