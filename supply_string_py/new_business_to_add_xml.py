# 业务中对字符串的操作（增删改查），用于业务string的迭代,同时会生成繁体文件

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
import string_xml_constants as SC
import string_tw_zh_convert as ZW 


# xml文件中的节点名称
attribName = 'name'  # --ID
attribLocation = 'location' # -->location
attribStringType = 'stringType'  # --> btns  pages msgs
attribOperateType = 'operateType'  # -->操作类型

# 操作类型 添加 更新 删除
operateTypeAdd = 'A'
operateTypeUpdate = 'U'
operateTypeDelete = 'D'

# 字符串位置 android（ supplyBase baseModule  buy）ios（base  buy）
locationSupplyBase = '0'
locationBaseModule = '1'
lcoationBuy = '2'

# 字符串类型  btns  pages msgs
stringTypeBtns='B'
stringTypePages='P'
stringTypeMsgs='M'
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
        isRemove=False
        for xmlElem in xmlTree.iter(tag='string'):
            xmlId=xmlElem.attrib['name']
            if id==xmlId:
                xmlRoot.remove(xmlElem)
                isRemove=True
        if isRemove:
            xmlTree.write(newPath, encoding='UTF-8', xml_declaration=True)

# 判断是那种操作类型 增加 删除  更新
def dealPathString(path, id, stringType, operateType, text):
    if operateType == operateTypeAdd:
        # add stirng to supplybase
        addString(path,id,stringType,text)

    elif operateType == operateTypeUpdate:
            # 打开文件删除指定的ID，并且key+1添加新字符
        deleteString(path, id, stringType)
        pattern = r'_v(?P<VERSION>\d)'
        # gyl_msg_shop_v1
        match=re.search(pattern,id)
        versionCode = match.group('VERSION')
        # 目前不使用版本号进行控制管理 采用key和中文value值进行判断
        # newVersion= int(versionCode)+1
        newVersion= int(versionCode)
        
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

#   string ID 进行拼装  gyl_msg_...._v1
def stringIdAssembly(stringType, stringId):
    if stringType == stringTypeBtns:
        return  SC._sourcePrefixBtn+stringId+SC._sourceVerion
    if stringType == stringTypePages:
        return SC._sourcePrefixPage+stringId+SC._sourceVerion
    if stringType == stringTypeMsgs:
        return SC._sourcePrefixMsg+stringId+SC._sourceVerion

    return ""
# 根据传入的文件路径解析需要新添加的字符串
# 字符变更（模块:基础模块(SupplyBase)–>【 0 】,公用模块(BaseModule)–> 【 1】,采购平台【 2 】 ,
# 字符串分类：btn–>【B】page-->【P】msg–>【 M】 
#  操作类型: 添加 -->【 A】  修改 -->【U】 删除 -->【D】）

# <root >
# 0 基础模块（SupplyBase） 1 公用模块(BaseModule) 2(采购平台)  supplyBase 和 BaseModule 的划分需要Android这边来负责
# <string name = "gyl_msg_menu_unit_default_v1" location = "0" stringType = 'B' operateType = "A" > 份 | 例 | 瓶 | 个 | 杯 </string >
# <string name = "gyl_msg_menu_unit_default_v1" location = "1" stringType = 'P' operateType = "U" > 更新键 </string >
# <string name = "gyl_msg_menu_unit_default_v1" location = "2" stringType = 'M' operateType = "D" > 删除键 </string >
# </root >

def xmlParse(path):
    xmlTree = ET.parse(path)
    for xmlElem in xmlTree.iter(tag='string'):
        stringId = xmlElem.attrib[attribName]
        try:
            stringLocation = xmlElem.attrib[attribLocation]
        except KeyError:
            print('文本未显示location,设置默认值为    1-->baseModule')
            stringLocation='1'
        
        try:
            stringType = xmlElem.attrib[attribStringType]
        except KeyError:
            print('文本未显示StringType,设置默认值为    C-->msg')
            stringType = 'C'

        try:
            stringOperateType = xmlElem.attrib[attribOperateType]
        except KeyError:
            print('文本未显示OperateType,设置默认值为    A-->add')
            stringOperateType = 'A'
        stringValue = xmlElem.text
        if stringOperateType == operateTypeAdd :
            stringId=stringIdAssembly(stringType,stringId)
        dealWithString(stringId, stringLocation, stringType,
                       stringOperateType, stringValue)

def   changeVersion(path):
        file = open(path, 'r')
        while 1:
            line = file.readline()
            if not line:
                file.close
                break
            # line中是否包含某个字符串
            if line.find('VERSION_CODE') != -1:
                splitList = str.split(line,'=')
                line = line.replace(splitList[1], ' 068')
                print(line)
                # for value in splitList:  # 循环输出列表值
                #     print(line)
# 入口函数 解析xml文件进行添加
def xmlConvertToAddString(path):
    xmlParse(path)
    # changeVersion(SC.baseUri+'/BaseString/gradle.properties')

# self test
if __name__ == "__main__":
    xmlConvertToAddString(SC._su_string_file_path)
