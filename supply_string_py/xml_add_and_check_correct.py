# xml  add 并且进行check文件的正确性

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os
import new_business_to_add_xml as ADD

import check_basic_zh_other_xml_correct as CHECK
import string_xml_constants as SC
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
import string_tw_zh_convert as ZW


def add(path):
    ADD.xmlConvertToAddString(path)

def check():
    CHECK.pathTransformAndToCheck()

def formatXml():
    for basicpath in SC._basicPathList:
        for basicTypePath in SC._basicTypeList:
            for sourrceSuffixPath in SC._sourceSuffixList:
                # 重写所有文件
                path=basicpath+basicTypePath+sourrceSuffixPath
                xmlTree = ET.parse(path)
                xmlTree.write(path, encoding='UTF-8', xml_declaration=True)

                # 重新翻译繁体
                twpath = basicpath+SC._basicTypeTW+sourrceSuffixPath
                zhpath = basicpath+SC._basicTypeZH+sourrceSuffixPath
                converList = ZW.fileConvertTraditional(zhpath)
                twFile = open(twpath, 'w+')
                twFile.writelines(converList)
                twFile.close

if __name__ == "__main__": 
    add(SC._su_string_file_path)
    check()
    # formatXml()

