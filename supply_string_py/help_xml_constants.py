_help_node_title_pattern_key = 'KEY'
_help_node_title_pattern_version = 'VERSION_NAME'
_help_node_title_pattern_title = 'TITLE'

_help_node_b_pattern_value = 'B_VALUE'

_help_node_first_pattern_value = 'FIRST_VALUE'
_help_node_second_pattern_value = 'SECOND_VALUE'
_help_node_third_pattern_value = 'THIRD_VALUE'
_help_node_foot_pattern_value = 'FOOT_VALUE'

_help_node_title_pattern = r'<(?P<KEY>\w+)(.*)version=\"(?P<VERSION_NAME>\w[0-9])"(.*)name=\"(?P<TITLE>.*)\"'

_help_node_title_version_pattern = r'version(.*)name'

_help_node_b_pattern = r'<b>(?P<B_VALUE>.*)</b>'

_help_node_first_pattern = r'    ▪︎︎(?P<FIRST_VALUE>.*)'
_help_node_first_pattern_1 = r'   ︎︎︎︎ ▪︎︎(?P<FIRST_VALUE>.*)'
_help_node_first_pattern_2 = r'▪︎︎(?P<FIRST_VALUE>.*)'
_help_node_second_pattern = r'        ▫︎(?P<SECOND_VALUE>.*)'
_help_node_third_pattern = r'            ৹(?P<THIRD_VALUE>.*)'
_help_node_foot_pattern = r'^\</(?P<FOOT_VALUE>.*)>'

# 生成的excel文件每个语言包括key位于的表格位置 后面语言添加时需要在这里注明语言的位置
_sheet_title_key_location = 'A'
_sheet_title_zh_location = 'B'
_sheet_title_en_location = 'C'
_sheet_title_thai_location = 'D'
# 容错处理时标注的位置
_sheet_title_error_location = 'E'

# 各个语言在excel文件中对应的 列
_EXCEL_MAPPING_ZH_LOCATON = 1
_EXCEL_MAPPING_EN_LOCATON = 2
_EXCEL_MAPPING_THAI_LOCATON = 3

# 文件类型
_FILE_TYPE_ZH_SOURCE = 'zh_source'
_FILE_TYPE_ZH = 'zh'
_FILE_TYPE_EN = 'en'
_FILE_TYPE_THAI = 'thai'

#  翻译文件 excel
_TRANSLATE_EXCEL_PATH = '/Users/hehongqing/Downloads/supply_help_string_thai.xlsx'
# _TRANSLATE_EXCEL_PATH = '/Users/hehongqing/Downloads/help/supply_help_string_thai3.xlsx'
# _TRANSLATE_EXCEL_PATH = '/Users/hehongqing/Downloads/help/supply_help_string_to_translate.xlsx'

# 带翻译文件
_TO_TRANSLATE_EXCEL_PATH = '/Users/hehongqing/Downloads/help/supply_help_string_to_translate.xlsx'

# 中文 最新文件位置
_SOURCE_ZH_PATH = r'/Users/hehongqing/workspace/utilsmaven/static_help/resources/xml/SupplyHelpFiles.xml'
# 中文最新 对应生成 key-value 的文件
_SOURCE_ZH_KEY_PATH = r'/Users/hehongqing/Downloads/help/test_help_key_source.xml'

# 中文文件位置
# 源文件
# _SOURCE_ZH_PATH = r'/Users/hehongqing/workspace/utilsmaven/static_help/resources/xml/SupplyHelpFiles.xml'
# 由  excel 文件生成的 zh
_SOURCE_EXCEL_ZH_PATH = r'/Users/hehongqing/Downloads/help/zh_help_excel.xml'
# 由  excel 文件生成的 zh 对应生成 key-value 的文件
_TEMP_ZH_KEY_PATH = r'/Users/hehongqing/Downloads/help/zh_help_key.xml'
# 比较后生成的最后文件
_TEMP_ZH_RESULT_PATH = r'/Users/hehongqing/Downloads/help/result_zh_help.xml'

# 英文文件位置
# 源文件
_SOURCE_EN_PATH = r'/Users/hehongqing/workspace/utilsmaven/static_help/resources/xml/SupplyHelpENFiles.xml'
# 由  excel 文件生成的 en
_SOURCE_EXCEL_EN_PATH = r'/Users/hehongqing/Downloads/help/en_help_excel.xml'
# 由  excel 文件生成的 en 对应生成 key-value 的文件
_TEMP_EN_KEY_PATH = r'/Users/hehongqing/Downloads/help/en_help_key.xml'
# 比较后生成的最后文件
_TEMP_EN_RESULT_PATH = r'/Users/hehongqing/Downloads/help/result_en_help.xml'

# 泰文文件位置
# 源文件
_SOURCE_THAI_PATH = r'/Users/hehongqing/workspace/utilsmaven/static_help/resources/xml/SupplyHelpTHFiles.xml'
# 由  excel 文件生成的 thai
_SOURCE_EXCEL_THAI_PATH = r'/Users/hehongqing/Downloads/help/thai_help_excel.xml'
# 由  excel 文件生成的 thai 对应生成 key-value 的文件
_TEMP_THAI_KEY_PATH = r'/Users/hehongqing/Downloads/help/thai_help_key.xml'
# 比较后生成的最后文件
_TEMP_THAI_RESULT_PATH = r'/Users/hehongqing/Downloads/help/result_thai_help.xml'

# 繁体文件位置
# 源文件
_SOURCE_TW_PATH = r'/Users/hehongqing/workspace/utilsmaven/static_help/resources/xml/SupplyHelpTWFiles.xml'
