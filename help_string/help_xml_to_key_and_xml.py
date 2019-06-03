# 将 help xml 文件转为带键值 key-value 的形式
# 颜色

from help_string import help_xml_constants as HC, help_xml_parse_utils as H_UTILS

# <WarehouseManagerViewHelp version="V1" name="仓库管理">
#     <![CDATA[
# <b>添加仓库</b>
#     ▪︎︎点添加按钮，可添加新的仓库。

# <b>供货仓库</b>
#     ▪︎︎仓库可设置为供货仓库。
#     ▪︎︎设置为供货仓库的仓库，门店在创建采购单和退货单时，可指定向该仓库进行采购或退货。
#     ▪︎︎总部可设置多个供货仓库，也可不设置任何供货仓库。不设置供货仓库时，门店仍可向总部采购，只是不能指定向哪个仓库采购。
#     ]]>
# </WarehouseManagerViewHelp

# 转化为---》》

# øøøøkey = WarehouseManagerViewHelp_V1øøøø < WarehouseManagerViewHelp version = "V1" name = "仓库管理" >
# <![CDATA[
#     øøøøkey = WarehouseManagerViewHelpV1_Aøøøø < b > 添加仓库 < /b >
#     øøøøkey= WarehouseManagerViewHelpV1_A_1øøøø    ▪︎︎点添加按钮，可添加新的仓库。

#     øøøøkey = WarehouseManagerViewHelpV1_Bøøøø < b > 供货仓库 < /b >
#     øøøøkey= WarehouseManagerViewHelpV1_B_1øøøø    ▪︎︎仓库可设置为供货仓库。
#     øøøøkey= WarehouseManagerViewHelpV1_B_2øøøø    ▪︎︎设置为供货仓库的仓库，门店在创建采购单和退货单时，可指定向该仓库进行采购或退货。
#     øøøøkey= WarehouseManagerViewHelpV1_B_3øøøø    ▪︎︎总部可设置多个供货仓库，也可不设置任何供货仓库。不设置供货仓库时，门店仍可向总部采购，只是不能指定向哪个仓库采购。
# ]] >
# </WarehouseManagerViewHelp >


xmlList=[]
# 文件读取结束时进行文件的输出 ：格式  key---value
def  fileOperateFinish(type): 
    global xmlList
    if type == HC._FILE_TYPE_ZH:
        file=open(HC._TEMP_ZH_KEY_PATH,'w+')
    elif type == HC._FILE_TYPE_ZH_SOURCE:
        file=open(HC._SOURCE_ZH_KEY_PATH,'w+')
    elif type == HC._FILE_TYPE_EN:
        file=open(HC._TEMP_EN_KEY_PATH,'w+')
    elif type == HC._FILE_TYPE_THAI:
        file=open(HC._TEMP_THAI_KEY_PATH,'w+')
    for  line in xmlList:
        file.write(line)
    file.close()

    xmlList.clear()


def readFile(filePath, type):
    file = open(filePath)
    while 1:
        line = file.readline()
        if not line:
            file.close

            fileOperateFinish(type)
            break
        else:
            # 读取到的每行
            # print(line)

            xml_key, xml_value = H_UTILS.dealLine(line)
            appendKeyLine(xml_key, line)


# 根据key---value 添加至 xmlList 当中
def  appendKeyLine(key,line):
    global xmlList
    # 如果这一行不含有\n 则认为这一行源数据输入不正确，需要校正(最后一行除外)
    if not '\n' in line and  not'</root>' in line:
            line=line+'\n'
    if key=='':
        xmlList.append(line)
    else: 
        xmlList.append('øøøøkey='+key+'øøøø'+line)


def xmlParseToKeyValueXml():
    
    readFile(HC._SOURCE_ZH_PATH, HC._FILE_TYPE_ZH_SOURCE)
    readFile(HC._SOURCE_EXCEL_ZH_PATH, HC. _FILE_TYPE_ZH)
    readFile(HC._SOURCE_EXCEL_EN_PATH, HC._FILE_TYPE_EN)
    readFile(HC._SOURCE_EXCEL_THAI_PATH, HC. _FILE_TYPE_THAI)




def  xmlParseToKeySourceValueXml():

    readFile(HC._SOURCE_ZH_PATH, HC._FILE_TYPE_ZH_SOURCE)
    readFile(HC._SOURCE_ZH_PATH, HC. _FILE_TYPE_ZH)
    readFile(HC._SOURCE_EN_PATH, HC._FILE_TYPE_EN)
    readFile(HC._SOURCE_THAI_PATH, HC. _FILE_TYPE_THAI)
if __name__ == "__main__":
    xmlParseToKeyValueXml()

