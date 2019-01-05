# 用于解析help xml的工具类

# 将 help xml 文件转为带键值key-value的形式
import re
import os
from openpyxl.workbook import Workbook
# 颜色
from openpyxl.styles import PatternFill
from openpyxl.styles import Color, Fill, Font, colors, Border, Side, Alignment
from openpyxl.cell import Cell

import help_xml_constants as HC

# WarehouseManagerViewHelp
_help_key = None

# V1
_help_key_version = None

# 是否已经初始化key
_init_key = False

# 第一个节点拼接值 【A-Z】
# A-Z
_key_first_node = None

# 第二个节点拼接值 【1...】
# 1...
_key_second_node = None

# 第三个节点拼接值 【a-z】
# a-z
_key_third_node = None


# 第四个节点拼接值 【1...】
# 1...
_key_fourth_node = None


# 特殊节点拼接值 【1...】
# 1...
_special_node = None

# 特殊行进行特殊的标识
SPECIAL_FLAG = 'SP'


INVALID_STRING_1 = '    <![CDATA['
INVALID_STRING_2 = '    ]]>'
STRING_CONNECTOR = '_'


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

# excel 输出结构
#  key                              value                               en
#  key_version                      title
#  WarehouseManagerViewHelp_V1      仓库管理
#  key_A_0                          添加仓库（截取掉<b>*</b>）
#  key_A_1                          点添加按钮，可添加新的仓库。(截取掉    ▪︎︎)
#  key_B_0                          供货仓库（截取掉<b>*</b>）
#  key_B_1                          仓库可设置为供货仓库。(截取掉    ▪︎︎)
#  ...依次递加



# 解析 help
# 返回参数： xml_key, xml_value
def dealLine(line):
    global _init_key, _help_key, _key_first_node, _key_second_node, _key_third_node, _key_fourth_node, _special_node, _help_key_version
    if _init_key == False and _help_key == None:
        match = re.search(HC._help_node_title_version_pattern, line)
        #  pattern  <WarehouseManagerViewHelp version="V1" name="仓库管理">
        if not match == None:
            _init_key = True
            # print(match)
            nodeTitleMatch = re.search(HC._help_node_title_pattern, line)
            # print(nodeTitleMatch)
            # print('key          '+nodeTitleMatch.group(HC._help_node_title_pattern_key))

            _help_key = nodeTitleMatch.group(HC._help_node_title_pattern_key)

            nodeVersion = nodeTitleMatch.group(
                HC._help_node_title_pattern_version)
            # print('VersionName  '+nodeVersion)

            _help_key_version = nodeVersion

            nodeTitleValue = nodeTitleMatch.group(
                HC._help_node_title_pattern_title)
            # print('Title        '+nodeTitleValue)
            excel_key_title = _help_key+STRING_CONNECTOR+_help_key_version

            return excel_key_title, nodeTitleValue
        else:
            return '', line
    elif INVALID_STRING_1 in line or INVALID_STRING_2 in line or line == '\n' or not re.search(r'^ *\n', line) == None or '<![CDATA[' in line or not re.search(r'	]]>', line) == None or ']]>'in line:
        # print('无效返回')
        return '', line
    elif not re.search(HC._help_node_b_pattern, line) == None:
        # pattern <b>添加仓库</b>
        nodeMatch = re.search(HC._help_node_b_pattern, line)
        # first_node_value = nodeMatch.group(HC._help_node_b_pattern_value)
        b_node_value = nodeMatch.group(HC._help_node_b_pattern_value)

        if _key_first_node == None:
            _key_first_node = 'A'
            # print(b_node_value)
            # 在这里输出 excel 第一个子节点  excel_key_node--->b_node_value
            excel_key_node = _help_key+_help_key_version+STRING_CONNECTOR+_key_first_node
            return excel_key_node, b_node_value
        else:
            # A+1
            # 同时需要将节点 置为初始值
            _key_second_node = None
            _key_third_node = None
            _key_fourth_node = None

            _key_first_node = chr(ord(_key_first_node)+1)
            # 在这里输出 excel 第一个子节点  excel_key_node--->first_node_value
            excel_key_node = _help_key+_help_key_version+STRING_CONNECTOR+_key_first_node

            return excel_key_node, b_node_value

    elif not re.search(HC._help_node_first_pattern, line) == None:
        # pattern'    ▪︎︎请按照标准格式说出您想要采购的原料及其数量。'
        secondNodeMatch = re.search(HC._help_node_first_pattern, line)
        # print(secondNodeMatch)
        # second_node_value = secondNodeMatch.group(HC._help_node_first_pattern_value)
        first_node_value = secondNodeMatch.group(
            HC._help_node_first_pattern_value)

        if _key_second_node == None:
            _key_second_node = 1
            # print(_help_key+'_'+_key_first_node+'_'+str(_key_second_node))

        else:
            _key_second_node += 1
            _key_third_node = None
            _key_fourth_node = None
            # print(first_node_value)
        # 这里输出excel 子节点的节点 excel_key_child_node---> first_node_value
        excel_key_child_node = _help_key+_help_key_version+STRING_CONNECTOR + \
            _key_first_node+STRING_CONNECTOR+str(_key_second_node)

        return excel_key_child_node, first_node_value
    elif not re.search(HC._help_node_first_pattern_1, line) == None:
            # pattern'    ▪︎︎请按照标准格式说出您想要采购的原料及其数量。'
        secondNodeMatch = re.search(HC._help_node_first_pattern_1, line)
        # print(secondNodeMatch)
        # second_node_value = secondNodeMatch.group(HC._help_node_first_pattern_value)
        first_node_value = secondNodeMatch.group(
            HC._help_node_first_pattern_value)

        if _key_second_node == None:
            _key_second_node = 1
            # print(_help_key+'_'+_key_first_node+'_'+str(_key_second_node))

        else:
            _key_second_node += 1
            _key_third_node = None
            _key_fourth_node = None
            # print(first_node_value)
        # 这里输出excel 子节点的节点 excel_key_child_node---> first_node_value
        excel_key_child_node = _help_key+_help_key_version+STRING_CONNECTOR + \
            _key_first_node+STRING_CONNECTOR+str(_key_second_node)

        return excel_key_child_node, first_node_value
    elif not re.search(HC._help_node_first_pattern_2, line) == None:
            # pattern'    ▪︎︎请按照标准格式说出您想要采购的原料及其数量。'
        secondNodeMatch = re.search(HC._help_node_first_pattern_2, line)
        # print(secondNodeMatch)
        # second_node_value = secondNodeMatch.group(HC._help_node_first_pattern_value)
        first_node_value = secondNodeMatch.group(
            HC._help_node_first_pattern_value)

        if _key_second_node == None:
            _key_second_node = 1
            # print(_help_key+'_'+_key_first_node+'_'+str(_key_second_node))

        else:
            _key_second_node += 1
            _key_third_node = None
            _key_fourth_node = None
            # print(first_node_value)
        # 这里输出excel 子节点的节点 excel_key_child_node---> first_node_value
        excel_key_child_node = _help_key+_help_key_version+STRING_CONNECTOR + \
            _key_first_node+STRING_CONNECTOR+str(_key_second_node)

        return excel_key_child_node, first_node_value
    elif not re.search(HC._help_node_second_pattern, line) == None:
        # pattern '        ▫︎如：胡萝卜采购100斤'
        nodeMatch = re.search(HC._help_node_second_pattern, line)
        second_node_value = nodeMatch.group(HC._help_node_second_pattern_value)
        # print('second_node_value'+second_node_value)
        if _key_third_node == None:
            _key_third_node = 'a'
        else:
            # a+1
            _key_third_node = chr(ord(_key_third_node)+1)
            _key_fourth_node = None
        # 这里输出excel 子节点的节点 excel_key_child_node---> fourth_node_value

        excel_key_child_node = _help_key+_help_key_version+STRING_CONNECTOR+_key_first_node + \
            STRING_CONNECTOR+str(_key_second_node) + \
            STRING_CONNECTOR+_key_third_node

        return excel_key_child_node, second_node_value

    elif not re.search(HC._help_node_third_pattern, line) == None:
        # pattern '            ৹【原料名称】为【胡萝卜】'
        nodeMatch = re.search(HC._help_node_third_pattern, line)
        third_node_value = nodeMatch.group(HC._help_node_third_pattern_value)

        # print('third_node_value'+third_node_value)
        if _key_fourth_node == None:
            _key_fourth_node = 1
        else:
            #    _key_fourth_node= int(_key_fourth_node)
           _key_fourth_node += 1
        # 这里输出excel 子节点的节点 excel_key_child_node---> fourth_node_value
        excel_key_child_node = _help_key+_help_key_version+STRING_CONNECTOR+_key_first_node+STRING_CONNECTOR + \
            str(_key_second_node)+STRING_CONNECTOR+_key_third_node + \
            STRING_CONNECTOR+str(_key_fourth_node)

        return excel_key_child_node, third_node_value

    elif not re.search(HC._help_node_foot_pattern, line) == None:
        nodeRootMatch = re.search(HC._help_node_foot_pattern, line)
        # pattern </StoreHouseListViewHelp>  != root
        value = nodeRootMatch.group(HC._help_node_foot_pattern_value)
        if not value == 'root':
            # 重置参数
            _help_key = None
            _help_key_version = None
            _init_key = False
            _key_first_node = None
            _key_second_node = None
            _special_node = None
            # print(value)
            return '', line
        else:
            # 文件读取结束
            return '', line
    else:
        # print(elif not re.search(r'(^\x00-\xff)!',line)==None:
        print('***************************匹配纯文字**************************'+line)
        line = re.sub(r'\n', '', line)
        # line = re.sub(r' *', '', line)
        print('***************************匹配纯文字**************************'+line)

        if _special_node == None:
            _special_node = 1
        else:
            _special_node += 1
        if not _key_first_node == None:
            excel_key_child_node = _help_key+_help_key_version+STRING_CONNECTOR + \
                SPECIAL_FLAG+STRING_CONNECTOR + \
                str(_special_node)+STRING_CONNECTOR+'A_'
        else:
            # 这里输出excel 子节点的节点 excel_key_child_node---> fourth_node_value
            excel_key_child_node = _help_key+_help_key_version+STRING_CONNECTOR + \
                SPECIAL_FLAG+STRING_CONNECTOR+str(_special_node)
        return excel_key_child_node, line
