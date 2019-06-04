# 国际化版本 查找出未翻译的 并在主干上查找替换翻译

# ! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 思路 1. 国际化版本中的中文版本解析出 KEY
#     2. 根据key进行查找国际化翻译文件对应的节点  Y 写入跳过
#           N  在主干文件中查找对应的KEY对应节点  Y 复制写入 N 打印出未翻译

from normal_string import string_xml_constants as SC
import xml.etree.ElementTree as ET
import logging

def xml_parse(basic_path,*internal_path):
    tree = ET.parse(basic_path)
    logging.debug()
    for elem in tree.iter(tag="string"):
        key = elem.attrib['name']
    # for i_pth in internal_path:




if __name__ == '__main__':
    xml_parse(SC._base_zh_btns_path)
