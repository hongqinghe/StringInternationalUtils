# 文件中的简体转化为繁体操作 返回list集合
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from help_string import help_xml_constants as HC
from base_lib.langcv import Converter


def Traditional2Simplified(sentence):
    """
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    """
    sentence = Converter('zh-hans').convert(sentence)
    return sentence


def simplified2Traditional(sentence):
    """
    将sentence中的简体字转为繁体字
    :param sentence: 待转换的句子
    :return: 将句子中简体字转换为繁体字之后的句子
    """
    sentence = Converter('zh-hant').convert(sentence)
    # sentence = Converter('zh-hant').convert(sentence.decode('utf-8'))
    # sentence = sentence.encode('utf-8')
    return sentence


def dealLine(coverterList, line):
    traditional_sentence = simplified2Traditional(line)
    coverterList.append(traditional_sentence)
    print(traditional_sentence)


def readFile(filePath):
    file = open(filePath)
    coverterList = []
    while 1:
        line = file.readline()
        if not line:
            file.close
            break
        else:
            dealLine(coverterList, line)
    return coverterList


def fileConvertTraditional(filePath):
    return readFile(filePath)


def helpToConvertTw():
    convertList = fileConvertTraditional(HC._SOURCE_ZH_PATH)
    twFile = open(HC._SOURCE_TW_PATH, 'w+')
    twFile.writelines(convertList)
    twFile.close


if __name__ == "__main__":
    # simplified_sentence = 'adsad进行简体转化繁体操作sda'
    # print("进行简体转化繁体操作")
    # list=readFile(SC._base_zh_btns_path)

    # print(list)
    convertList = fileConvertTraditional(HC._SOURCE_ZH_PATH)
    twFile = open(HC._SOURCE_TW_PATH, 'w+')
    twFile.writelines(convertList)
    twFile.close