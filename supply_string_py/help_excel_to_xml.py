# # 帮助文档excel 转化为 xml
import re
import os

import  xlrd
import os
import macpath
import random

def getExceltable(excelPath):
    #打开excel文件
    data=xlrd.open_workbook(excelPath)     
    #获取第一张工作表（通过索引的方式）
    table=data.sheets()[0] 
    # 获取 sheet name
    sheetsNanme=table.name
    print('工作表名称'+sheetsNanme)
    return table

"""
table:          excelTable
type:           读取 help excel中的哪一列
resultFilePath: 输出文件的路径
"""
def  excelToXml(table,type,resultFilePath):
    # 获取表格的行数和列数
    nrows=table.nrows
    ncols=table.ncols
    print('行数：'+str(nrows))
    print('列数：'+str(ncols))

    fileInitContent1='<?xml version="1.0" encoding="utf-8"?>'
    fileInitContent2='<root>'
    fileInitContent3='</root>'
    file=open(resultFilePath,'a')
    file.write(fileInitContent1)
    file.write('\n'+fileInitContent2)
    _first_init=True
    xml_title=''
    _node_first=True

    for i in range(1,nrows):
        for j in range(ncols):
            tableCellKey=table.row(i)[j].value

            # print('每个单元格的值：'+str(tableCellKey))
            
            # pattern TDFTemplatePurchaseDetailHelp_V1
            titleMatch=re.search(r'(?P<TITLE>.*)_(?P<VERSION>V\d\Z)',tableCellKey)

            # pattern TDFTemplatePurchaseDetailHelp_A
            nodeMath=re.search(r'(?P<NODE_NAME>.*)_[A-Z]\Z',tableCellKey)

            # pattern TDFTemplatePurchaseDetailHelp_A_1
            childNodeMatch=re.search(r'(?P<CHILDE_NODE_NAME>.*)_[A-Z]_\d+\Z',tableCellKey)

            # pattern TDFGoodsPurchaseListViewControllerHelpTagOfChainMode_SP_1
            specialNodeMatch=re.search(r'(?P<SPECIAL_NODE_NAME>.*)_SP_\d+',tableCellKey)

            # pattern VoicePurchaseHelp_A_2_a
            childChildNopdeMatch=re.search(r'(?P<CHILD_CHILD_NODE_NAME>.*)_[A-Z]_\d+_[a-z]\Z',tableCellKey)

            # pattern VoicePurchaseHelp_A_2_a_1
            childChildChildNodeMatch=re.search(r'(?P<CHILD_CHILD_CHILD_NODE_NAME>.*)_[A-Z]_\d+_[a-z]_\d+\Z',tableCellKey)
            #  _first_init
            #  xml_title
            if not titleMatch==None:
                if _first_init==True:
                    _first_init=False
                    xml_title=titleMatch.group('TITLE')
                    version=titleMatch.group('VERSION')
                    print('xml  First title         '+xml_title+' xml first version '+ version)
                    #  读取该key  对应value
                    tableCellValue=table.row(i)[j+type].value
                    print(tableCellValue)
                    file.write('\n'+'<'+xml_title+' version=\"'+version+'\" name=\"'+tableCellValue+'\">'+'\n'+'    <![CDATA[')
                else:
                    _node_first=True
                    file.write('\n'+'    ]]>')
                    file.write('\n'+'</'+xml_title+'>'+'\n')
                    xml_title=titleMatch.group('TITLE')
                    version=titleMatch.group('VERSION')
                    print('xml  First title         '+xml_title+' xml first version '+ version)
                    #  读取该key  对应value
                    tableCellValue=table.row(i)[j+type].value
                    print(tableCellValue)

                    if xml_title=='TDFStoreAllocateListHelpTag':
                        print('****************************')
                    file.write('\n'+'<'+xml_title+' version=\"'+version+'\" name=\"'+tableCellValue+'\">'+'\n'+'    <![CDATA[')
                break
            elif not nodeMath==None:
                print('node       : ')
                print(nodeMath)
                nodeValue=table.row(i)[j+type].value
                print(nodeValue)

                if _node_first==True:
                    file.write('\n'+'<b>'+nodeValue+'</b>')
                    _node_first=False
                else:
                    _node_first=False
                    file.write('\n')
                    file.write('\n'+'<b>'+nodeValue+'</b>')
                break
            elif not childNodeMatch==None:
                print('child_node       : ')
                print(childNodeMatch)
                nodeValue=table.row(i)[j+type].value
                print(nodeValue)
                file.write('\n'+'    ▪︎︎'+nodeValue)
                break
            elif not specialNodeMatch==None:
                nodeValue=table.row(i)[j+type].value

                specialNodeMatchA=re.search(r'(?P<SPECIAL_NODE_NAME_A>.*)_SP_\d_A_\Z',tableCellKey)
                specialNodeMatchB=re.search(r'(?P<SPECIAL_NODE_NAME_A>.*)_SP_\d\Z',tableCellKey)
                
                if not specialNodeMatchA==None:
                    file.write('\n'+'    '+nodeValue)
                else:
                    file.write('\n\n'+nodeValue+'\n')
                # spKey=specialNodeMatch.group('SPECIAL_NODE_NAME')
                # print('special'+spKey)
                # print(nodeValue)
                break
            elif not childChildNopdeMatch==None:
                spKey=childChildNopdeMatch.group('CHILD_CHILD_NODE_NAME')
                print('special'+spKey)
                nodeValue=table.row(i)[j+type].value
                print(nodeValue)
                file.write('\n'+'        ▫︎'+nodeValue)
                break
            elif not childChildChildNodeMatch==None:
                spKey=childChildChildNodeMatch.group('CHILD_CHILD_CHILD_NODE_NAME')
                print('special'+spKey)
                nodeValue=table.row(i)[j+type].value
                print(nodeValue)
                file.write('\n'+'            ৹'+nodeValue)
                break
    file.write('\n'+'    ]]>')
    file.write('\n'+'</'+xml_title+'>')
    file.write('\n'+fileInitContent3)
    file.close

path='/Users/hehongqing/Downloads/help_string.xlsx'
xmlPath='/Users/hehongqing/Downloads/help_string.xml'
en_xml_path='/Users/hehongqing/Downloads/en_help_string.xml'

help_zh_path = '/Users/hehongqing/WorkSpace/Android/static_help/resources/xml/SupplyHelpFiles.xml'

# 生成的文件和本地xml文件进行比较
def compareXmlWithLocal(xmlPath,type):
    file = open(xmlPath,'r+')
    count=linecount_1(xmlPath)
    print(count)
    # 根据行读出文件
    while 1:
        line = file.readline()
        if not line:
            file.close
            break
        else:
            # 读取到的每行
            # print(line)
            dealLine(file,line, type)


def dealLine(file,line,type):
    sourceFile=open(help_zh_path)
    
    while 1:
        sourceLine = sourceFile.readline()
        if not line:
            sourceFile.close
            break
        else:
            # 读取到的每行
            if not  sourceLine==line:
                print(file.tell())
                print(sourceLine)
                print(file.seek(0,1))
                file.write
def linecount_1(path):
    return len(open(path).readlines())#最直接的方法
def  writePosition():           
    lines=[]
    f=open("d:\\1script\\1.txt",'r')  #your path!
    for line in f:
        lines.append(line)
    f.close()
    print(lines)
    lines.insert(3,"666\n")           #第四行插入666并回车
    s=''.join(lines)
    f=open("d:\\1script\\1.txt",'w+') #重新写入文件
    f.write(s)
    f.close()
    del lines[:]                      #清空列表
    print(lines)

    
def excleConversionXml():
    table=getExceltable(path)
    # 生成 zh_xml 文件
    # excelToXml(table,1,xmlPath)
    # # 生成 en_xml 文件
    # excelToXml(table,2,en_xml_path)

    compareXmlWithLocal(xmlPath,1)

if __name__ == "__main__":
    excleConversionXml()
        