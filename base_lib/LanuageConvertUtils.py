# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 国际化转化 Utils


# 处理  ModuleNotFoundError: No module named
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)

from langcv import Converter
import logging
def __simplified_2_traditional(sentence):
    """
    将sentence中的简体字转为繁体字
    :param sentence: 待转换的句子
    :return: 将句子中简体字转换为繁体字之后的句子
    """
    sentence = Converter('zh-hant').convert(sentence)
    return sentence


def __deal_line(result_list, line):
    traditional_sentence = __simplified_2_traditional(line)
    result_list.append(traditional_sentence)
    # print(traditional_sentence)


def __write_file(file, line_list):
    file = open(file, 'w+')
    if file is not None:
        file.writelines(line_list)
        file.close()
        print("     目标文件翻译结束，请查看>>>>", file.name, "<<<<文件")
    else:
        print("     文件初始化失败")


def __read_file(file_path):
    file = open(file_path)
    print("     开始读取文件")
    result_list = []
    while 1:
        line = file.readline()
        if not line:
            file.close()
            break
        else:
            __deal_line(result_list, line)
    print("     准备写入文件")
    return result_list


def convert_zh_to_tw(target_file, result_file):
    """
        中文简体文件翻译为中文繁体
    :param target_file: 需要转化的文件
    :param result_file: 转化后的文件
    :return: None
    """
    logging.debug("----->开始翻译文件")
    result_list = __read_file(target_file)
    if result_list is not None:
        __write_file(result_file, result_list)
    else:
        logging.error("----->无法找到需要写入的内容，请查看输入的文件内容完整")

if __name__ == '__main__':
    # logging.basicConfig()
    baseUri = '/Users/hehongqing/WorkSpace/utilsMaven/GYLStringModule'
    _supply_base_zh_btn_path = baseUri + '/SupplyBaseString/src/main/res/values/btns.xml'
    convert_zh_to_tw(_supply_base_zh_btn_path,
                     r'/Users/hehongqing/Downloads/international/string/btn_tw.xml')
