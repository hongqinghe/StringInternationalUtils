# xml  add 并且进行check文件的正确性

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

import xml.etree.ElementTree as ET
from normal_string import string_tw_zh_convert as ZW, string_xml_constants as SC, \
    new_business_to_add_xml as ADD, check_basic_zh_other_xml_correct as CHECK
import base_lib.LanuageConvertUtils as LANG

def add(path):
    ADD.xmlConvertToAddString(path)


def check():
    CHECK.pathTransformAndToCheck()


def formatXml():
    for basicPath in SC._basicPathList:
        for basicTypePath in SC._basicTypeList:
            for sourrceSuffixPath in SC._sourceSuffixList:
                # 重写所有文件
                path = basicPath + basicTypePath + sourrceSuffixPath
                xmlTree = ET.parse(path)
                xmlTree.write(path, encoding='UTF-8', xml_declaration=True)

                # 重新翻译繁体
                tw_path = basicPath + SC._basicTypeTW + sourrceSuffixPath
                zh_path = basicPath + SC._basicTypeZH + sourrceSuffixPath
                LANG.convert_zh_to_tw(zh_path,tw_path)



if __name__ == "__main__":
    add(SC._su_string_file_path)
    check()
    # formatXml()
