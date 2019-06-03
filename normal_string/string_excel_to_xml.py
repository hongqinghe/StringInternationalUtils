#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  将 string 对应的excel 转化为xml文件
import os

import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, ElementTree
import xlrd
from normal_string import string_xml_constants as SC
from time import time

excelPath = '/Users/hehongqing/Downloads/help/supply_string_result.xlsx'
# excelPath = '/Users/hehongqing/Downloads/supply_base_btn_thai.xlsx'


fileSuffixBtn = '/btns_temp.xml'
fileSuffixPage = '/pages_temp.xml'
fileSuffixMsg = '/msgs_temp.xml'

zh_type = 1
en_type = 2
thai_type = 3
# 存贮 key 为sheetName 的集合
_tables = None

# 通过传入的excel 获取所有的sheet 
def getExceltable(excelPath):
    # 打开excel文件
    tables = {}
    data = xlrd.open_workbook(excelPath)
    for sheetName in data._sheet_names:
        tables.setdefault(sheetName, data.sheet_by_name(sheetName))
    return tables

# 通过  excel 解析出的xml  key，查找对应源文件中的element对象

def keyHomologousElement(searchTree, key):
    # tree=getXMLTree(searchTree)
    for elem in searchTree.iter(tag='string'):
        # print(elem.attrib,elem.text)
        xmlKey = (elem.attrib)['name']
        if xmlKey == key:
            return elem

# 通过  excel 解析出的key和value，查找对应源文件中的element对象
def valueHomologousElement(searchTree,key, value):
    for elem in searchTree.iter(tag='string'):
        # print(elem.attrib,elem.text)
        xmlKey = (elem.attrib)['name']
        xmlValue = elem.text
        if xmlKey == key and xmlValue ==value:
            return elem

def getXMLTree(filePath):
    return ET.parse(filePath)


def toRestultXML(selfTable, tableNrows, tableNcols, searchTree, resultXMLPath,location):
    restultRootEN = Element('resources')
    restultTreeEN = ElementTree(restultRootEN)
    for i in range(1, tableNrows):
        tableCellKey = selfTable.row(i)[0].value
        # 校验第一次 只有源文件中的key、value 和excel 中的 key、value 相等的时候才进行输出
        resultElem = valueHomologousElement(
            searchTree, tableCellKey, selfTable.row(i)[1].value)

        # print(tableCellKey)
        if not resultElem == None:
            excelValue = selfTable.row(i)[location].value
            if excelValue == '':
                print('***************该项未翻译,对应key：     ' +
                      tableCellKey+'      ***************loaction  en(2)  thai(3) *************:'+str(location))
            else:
                resultElem.text = excelValue
                # print('excelValue    '+str( excelValue))
                restultRootEN.append(resultElem)
        try:
            restultTreeEN.write(resultXMLPath, encoding='utf-8',
                                        xml_declaration=True)
        except FileNotFoundError as fileError:
            print(fileError)
            

'''
    解析table
    selfTable: 对应sheet
    searchXMLFilePath: 需要匹配的源文件
    resultXMLPath:  输出的xml文件路径
    type: 对应表格的type 1：zh  2：EN  3：Thai
'''
def toTraverseTable(selfTable, resultXMLPath, searchXMLFilePath, type):
    tableNrows = selfTable.nrows
    tableNcols = selfTable.ncols

    searchTree = ET.parse(searchXMLFilePath)

    if type == en_type:
        loaction=2
        toRestultXML(selfTable, tableNrows, tableNcols,
                   searchTree, resultXMLPath, loaction)
    elif type==thai_type:
        loaction=3
        toRestultXML(selfTable, tableNrows, tableNcols,
                       searchTree, resultXMLPath, loaction)
# 初始化excel
def initExcel():
    global _tables
    _tables = getExceltable(excelPath)

# 返回指定的 table
# fileType sheetName
def getTableAndFileLocation(fileType, stringType):
    if fileType == SC._supply_base_sheet_head_btn:
        if stringType == zh_type:
            return _tables[fileType], SC._supplyBaseBasicPath+SC._basicTypeZH+fileSuffixBtn
        elif stringType == en_type:
            return _tables[fileType], SC._supplyBaseBasicPath+SC._basicTypeEN+fileSuffixBtn
        elif stringType == thai_type:
            return _tables[fileType], SC._supplyBaseBasicPath+SC._basicTypeThai+fileSuffixBtn
    elif fileType == SC._supply_base_sheet_head_msg:
        if stringType == zh_type:
            return _tables[fileType], SC._supplyBaseBasicPath+SC._basicTypeZH+fileSuffixMsg
        elif stringType == en_type:
            return _tables[fileType], SC._supplyBaseBasicPath+SC._basicTypeEN+fileSuffixMsg
        elif stringType == thai_type:
            return _tables[fileType], SC._supplyBaseBasicPath+SC._basicTypeThai+fileSuffixMsg

    elif fileType == SC._supply_base_sheet_head_page:
        if stringType == zh_type:
            return _tables[fileType], SC._supplyBaseBasicPath+SC._basicTypeZH+fileSuffixPage
        elif stringType == en_type:
            return _tables[fileType], SC._supplyBaseBasicPath+SC._basicTypeEN+fileSuffixPage
        elif stringType == thai_type:
            return _tables[fileType], SC._supplyBaseBasicPath+SC._basicTypeThai+fileSuffixPage
    elif fileType == SC._base_sheet_head_btn:
        if stringType == zh_type:
            return _tables[fileType], SC._baseBasicPath+SC._basicTypeZH+fileSuffixBtn
        elif stringType == en_type:
            return _tables[fileType], SC._baseBasicPath+SC._basicTypeEN+fileSuffixBtn
        elif stringType == thai_type:
            return _tables[fileType], SC._baseBasicPath+SC._basicTypeThai+fileSuffixBtn
    elif fileType == SC._base_sheet_head_msg:
        if stringType == zh_type:
            return _tables[fileType], SC._baseBasicPath+SC._basicTypeZH+fileSuffixMsg
        elif stringType == en_type:
            return _tables[fileType], SC._baseBasicPath+SC._basicTypeEN+fileSuffixMsg
        elif stringType == thai_type:
            return _tables[fileType], SC._baseBasicPath+SC._basicTypeThai+fileSuffixMsg
    elif fileType == SC._base_sheet_head_page:
        if stringType == zh_type:
            return _tables[fileType], SC._baseBasicPath+SC._basicTypeZH+fileSuffixPage
        elif stringType == en_type:
            return _tables[fileType], SC._baseBasicPath+SC._basicTypeEN+fileSuffixPage
        elif stringType == thai_type:
            return _tables[fileType], SC._baseBasicPath+SC._basicTypeThai+fileSuffixPage

    elif fileType == SC._buy_sheet_head_btn:
        if stringType == zh_type:
            return _tables[fileType], SC._buyBasicPath+SC._basicTypeZH+fileSuffixBtn
        elif stringType == en_type:
            return _tables[fileType], SC._buyBasicPath+SC._basicTypeEN+fileSuffixBtn
        elif stringType == thai_type:
            return _tables[fileType], SC._buyBasicPath+SC._basicTypeThai+fileSuffixBtn
    elif fileType == SC._buy_sheet_head_msg:
        if stringType == zh_type:
            return _tables[fileType], SC._buyBasicPath+SC._basicTypeZH+fileSuffixMsg
        elif stringType == en_type:
            return _tables[fileType], SC._buyBasicPath+SC._basicTypeEN+fileSuffixMsg
        elif stringType == thai_type:
            return _tables[fileType], SC._buyBasicPath+SC._basicTypeThai+fileSuffixMsg
    elif fileType == SC._buy_sheet_head_page:
        if stringType == zh_type:
            return _tables[fileType], SC._buyBasicPath+SC._basicTypeZH+fileSuffixPage
        elif stringType == en_type:
            return _tables[fileType], SC._buyBasicPath+SC._basicTypeEN+fileSuffixPage
        elif stringType == thai_type:
            return _tables[fileType], SC._buyBasicPath+SC._basicTypeThai+fileSuffixPage


def traverse(stringType):
    if stringType == zh_type:
        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._supply_base_sheet_head_btn, stringType)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._supplybase_zh_btns_path, stringType)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._supply_base_sheet_head_page, stringType)

        toTraverseTable(selfTable, resultXMLPath,
                        SC._supplybase_zh_pages_path, stringType)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._supply_base_sheet_head_msg, stringType)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._supplybase_zh_msgs_path, stringType)

        # Base
        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._base_sheet_head_btn, zh_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._base_zh_btns_path, zh_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._base_sheet_head_page, zh_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._base_zh_pages_path, zh_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._base_sheet_head_msg, zh_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._base_zh_msgs_path, zh_type)

        # buy
        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._buy_sheet_head_btn, zh_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._buy_zh_btns_path, zh_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._buy_sheet_head_page, zh_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._buy_zh_pages_path, zh_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._buy_sheet_head_msg, zh_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._buy_zh_msgs_path, zh_type)
    elif stringType == en_type:
        # supplyBase
        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._supply_base_sheet_head_btn, en_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._supplybase_zh_btns_path, en_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._supply_base_sheet_head_page, en_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._supplybase_zh_pages_path, en_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._supply_base_sheet_head_msg, en_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._supplybase_zh_msgs_path, en_type)

        # Base
        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._base_sheet_head_btn, en_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._base_zh_btns_path, en_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._base_sheet_head_page, en_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._base_zh_pages_path, en_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._base_sheet_head_msg, en_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._base_zh_msgs_path, en_type)

        # buy
        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._buy_sheet_head_btn, en_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._buy_zh_btns_path, en_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._buy_sheet_head_page, en_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._buy_zh_pages_path, en_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._buy_sheet_head_msg, en_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._buy_zh_msgs_path, en_type)

    elif stringType == thai_type:
        # supplyBase
        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._supply_base_sheet_head_btn, thai_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._supplybase_zh_btns_path, thai_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._supply_base_sheet_head_page, thai_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._supplybase_zh_pages_path, thai_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._supply_base_sheet_head_msg, thai_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._supplybase_zh_msgs_path, thai_type)

        # Base
        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._base_sheet_head_btn, thai_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._base_zh_btns_path, thai_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._base_sheet_head_page, thai_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._base_zh_pages_path, thai_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._base_sheet_head_msg, thai_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._base_zh_msgs_path, thai_type)

        # buy
        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._buy_sheet_head_btn, thai_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._buy_zh_btns_path, thai_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._buy_sheet_head_page, thai_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._buy_zh_pages_path, thai_type)

        selfTable, resultXMLPath = getTableAndFileLocation(
            SC._buy_sheet_head_msg, thai_type)
        toTraverseTable(selfTable, resultXMLPath,
                        SC._buy_zh_msgs_path, thai_type)


def toGenerateResultXml(comparePath, targetPath, sourcePath):
    compareTree = ET.parse(comparePath)
    compareRoot = compareTree.getroot()
    sourceTree = getXMLTree(targetPath)
    for elem in compareTree.iter(tag='string'):
            # print(elem.attrib,elem.text)
        xmlKey = (elem.attrib)['name']
        # 解析 excel文件中可以在xml文件中已经没有了，则进行删除操作
        if keyHomologousElement(sourceTree, xmlKey) == None:
            print(elem)
            compareRoot.remove(elem)
    # 删除生成的临时文件
    os.remove(comparePath)
    # 写入 restult 文件
    compareTree.write(sourcePath, encoding='UTF-8', xml_declaration=True)


'''
检测数据是否最新 最后数据校验
解析 excel 文件中可能在 但是 xml 文件中已经没有了，则进行删除操作
'''


def checkXML(stringType):
    if stringType == zh_type:
        type = SC._basicTypeZH
        return
        # supplyBase
    elif stringType == en_type:
        type = SC._basicTypeEN
    elif stringType == thai_type:
        type = SC._basicTypeThai

    filePath = SC._supplyBaseBasicPath + '%s'+fileSuffixBtn
    filePath = filePath % (type)
    sourcePath = SC._supplyBaseBasicPath+'%s'+SC._sourceSuffixBtn
    sourcePath = sourcePath % (type)
    # print("sourcePath  Btn :"+sourcePath)
    toGenerateResultXml(
        comparePath=filePath, targetPath=SC._supplybase_zh_btns_path, sourcePath=sourcePath)

    filePath = SC._supplyBaseBasicPath + '%s'+fileSuffixPage
    filePath = filePath % (type)
    sourcePath = SC._supplyBaseBasicPath+'%s'+SC._sourceSuffixPage
    sourcePath = sourcePath % (type)
    # print("sourcePath  page :"+sourcePath)
    toGenerateResultXml(filePath, SC._supplybase_zh_pages_path, sourcePath)

    filePath = SC._supplyBaseBasicPath + '%s'+fileSuffixMsg
    filePath = filePath % (type)
    sourcePath = SC._supplyBaseBasicPath+'%s'+SC._sourceSuffixMsg
    sourcePath = sourcePath % (type)
    # print("sourcePath  Msg :"+sourcePath)
    toGenerateResultXml(filePath, SC._supplybase_zh_msgs_path, sourcePath)

    # base

    filePath = SC._baseBasicPath + '%s'+fileSuffixBtn
    filePath = filePath % (type)
    sourcePath = SC._baseBasicPath+'%s'+SC._sourceSuffixBtn
    sourcePath = sourcePath % (type)

    toGenerateResultXml(filePath, SC._base_zh_btns_path, sourcePath)

    filePath = SC._baseBasicPath + '%s'+fileSuffixPage
    filePath = filePath % (type)
    sourcePath = SC._baseBasicPath+'%s'+SC._sourceSuffixPage
    sourcePath = sourcePath % (type)
    toGenerateResultXml(filePath, SC._base_zh_pages_path, sourcePath)

    filePath = SC._baseBasicPath + '%s'+fileSuffixMsg
    filePath = filePath % (type)
    sourcePath = SC._baseBasicPath+'%s'+SC._sourceSuffixMsg
    sourcePath = sourcePath % (type)
    toGenerateResultXml(filePath, SC._base_zh_msgs_path, sourcePath)

    # buy
    filePath = SC._buyBasicPath + '%s'+fileSuffixBtn
    filePath = filePath % (type)
    sourcePath = SC._buyBasicPath+'%s'+SC._sourceSuffixBtn
    sourcePath = sourcePath % (type)
    toGenerateResultXml(filePath, SC._buy_zh_btns_path, sourcePath)

    filePath = SC._buyBasicPath + '%s'+fileSuffixPage
    filePath = filePath % (type)
    sourcePath = SC._buyBasicPath+'%s'+SC._sourceSuffixPage
    sourcePath = sourcePath % (type)
    toGenerateResultXml(filePath, SC._buy_zh_pages_path, sourcePath)

    filePath = SC._buyBasicPath + '%s'+fileSuffixMsg
    filePath = filePath % (type)
    sourcePath = SC._buyBasicPath+'%s'+SC._sourceSuffixMsg
    sourcePath = sourcePath % (type)
    toGenerateResultXml(filePath, SC._buy_zh_msgs_path, sourcePath)


def main():
    start = time()
    initExcel()

    # traverse(zh_type)
    # 解析excel结束后进行check操作(更新、删除比较)
    # checkXML(zh_type)

    traverse(en_type)
    # 解析excel结束后进行check操作(更新、删除比较)
    checkXML(en_type)
    # os.system('cd '+SC._supplyBaseBasicPath+'&&git add -A'+'&&git commit -m "excel_to_xml"')
    traverse(thai_type)
    checkXML(thai_type)
    elapsed = (time() - start)
    # print("Time used:", elapsed)


if __name__ == "__main__":
    main()
