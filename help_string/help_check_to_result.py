# help  xml文件做最后的check并生成最后的文件


import re

from help_string import help_xml_constants as HC, help_xml_parse_utils as H_UTILS

resultXML = []


def dealLine(line, xmlList):
    # 【key=*'+key+'*】'+line
    global resultXML
    match = re.search(r'(?P<KEY>øøøøkey=.*øøøø)(?P<LineContent>.*)', line)
    # value=re.search(r'.*',line)
    xmlLineContent = None
    helpContent = None
    if not match is None:
        # print(match.group('KEY'))
        helpKey = match.group('KEY')
        helpContent = match.group('LineContent')
        # print(match.group('LineContent'))
        for xmlLine in xmlList:
            if helpKey in xmlLine:
                # print(xmlLine)
                xmlMatch = re.search(
                    r'(?P<KEY>øøøøkey=.*øøøø)(?P<LineContent>.*)', xmlLine)
                if not xmlMatch == None:
                    xmlKey = xmlMatch.group('KEY')
                    if xmlKey == helpKey:
                        xmlLineContent = xmlMatch.group('LineContent')
                        # 这里是某一项未翻译，则获取中文中的值，避免为空
                        xmlKey, xmlLine = H_UTILS.dealLine(xmlLineContent)
                        if xmlLine == '':
                            xmlLineContent = match.group('LineContent')
                        break
    else:
        print(line)
        xmlKey, xmlLine = H_UTILS.dealLine(line)
        if xmlKey == '':
            xmlLineContent = line
    if xmlLineContent is None:
        xmlLineContent = helpContent

    resultXML.append(xmlLineContent)


# 根据源文件进行匹配 baseSourceXml 默认为中文为基础文件


def readSourceFile(baseSourceXml, xmlList, resultPath):
    file = open(baseSourceXml)
    while 1:
        line = file.readline()
        if not line:
            file.close
            createResultFile(resultPath)
            break
        else:
            dealLine(line, xmlList)


def readExcelConversionXml(compareXml, baseSourceXml, resultPath):
    file = open(compareXml)
    xmlList = []
    while 1:
        line = file.readline()
        if not line:
            file.close
            readSourceFile(baseSourceXml, xmlList, resultPath)
            break
        else:
            # 读取到的每行
            # print(line)
            xmlList.append(line)
    return xmlList


# 生成最终的文件
def createResultFile(resultPath):
    file = open(resultPath, 'w+')
    for line in resultXML:
        # print('*****************'+line)
        if not '\n' in line:
            line = line + '\n'
        file.write(line)
    file.close()


def checkToResultXml():
    global resultXML
    resultXML = []
    readExcelConversionXml(HC._TEMP_ZH_KEY_PATH,
                           HC._SOURCE_ZH_KEY_PATH, HC._TEMP_ZH_RESULT_PATH)
    resultXML = []
    readExcelConversionXml(HC._TEMP_EN_KEY_PATH,
                           HC._SOURCE_ZH_KEY_PATH, HC._TEMP_EN_RESULT_PATH)
    resultXML = []
    readExcelConversionXml(HC._TEMP_THAI_KEY_PATH,
                           HC._SOURCE_ZH_KEY_PATH, HC._TEMP_THAI_RESULT_PATH)


if __name__ == "__main__":
    checkToResultXml()
