# help  xml文件做最后的check并生成最后的文件
import re
import os
from openpyxl.workbook import Workbook
# 颜色
# 颜色
from openpyxl.styles import  PatternFill
from openpyxl.styles import Color, Fill,Font,colors,Border,Side,Alignment
from openpyxl.cell import Cell

import xlrd
from openpyxl.workbook import Workbook
import string_xml_to_excel as SE
import string_xml_constants as SC
from time import time

test_path = r'/Users/hehongqing/Downloads/test_help.xml'
test_path_key = r'/Users/hehongqing/Downloads/test_help_key.xml'
test_path_source = r'/Users/hehongqing/Downloads/test_help_key_source.xml'
resultPath = r'/Users/hehongqing/Downloads/result_help.xml'

resultXML=[]

def dealLine(line,xmlList):
# 【key=*'+key+'*】'+line
    global resultXML
    match=re.search(r'(?P<KEY>【key=.*】)(?P<LineContent>.*)',line)
    # value=re.search(r'.*',line)
    xmlLineContent=None
    helpContent=None
    if  not match==None:
        print(match.group('KEY'))
        helpKey=match.group('KEY')
        helpContent=match.group('LineContent')
        print(match.group('LineContent'))
        for xmlLine in  xmlList:
            if helpKey in xmlLine:
                print(xmlLine)
                xmlMatch=re.search(r'(?P<KEY>【key=.*】)(?P<LineContent>.*)',xmlLine)
                if not xmlMatch==None:
                    xmlKey=xmlMatch.group('KEY')
                    if xmlKey==helpKey:
                        xmlLineContent=xmlMatch.group('LineContent')
                        break
    else:
        print(line)
        xmlLineContent=line
    if xmlLineContent==None:
        xmlLineContent=helpContent
    resultXML.append(xmlLineContent)

def readSourceFile(sourcePath,xmlList):
    file=open(sourcePath)
    while 1:
        line = file.readline()
        if not line:
            file.close
            break
        else:
            # 读取到的每行
            # print(line)
            dealLine(line,xmlList)
def readExcelConversionXml(excelTXml):
    file=open(excelTXml)
    xmlList=[]
    while 1:
        line = file.readline()
        if not line:
            file.close
            break
        else:
            # 读取到的每行
            # print(line)
            xmlList.append(line)
    return xmlList
def createResultFile(resultPath):
    file=open(resultPath,'w+')
    for line in resultXML:
        print('*****************'+line)
        if not '\n' in line:
            line=line+'\n'
        file.write(line)
    file.close()

if __name__ == "__main__":
    xmlList= readExcelConversionXml(test_path_key)
    readSourceFile(test_path_source,xmlList)
    createResultFile(resultPath)
   

            


