_help_node_title_pattern_key='KEY'
_help_node_title_pattern_version='VERSION_NAME'
_help_node_title_pattern_title='TITLE'

_help_node_b_pattern_value='B_VALUE'

_help_node_first_pattern_value='FIRST_VALUE'
_help_node_second_pattern_value='SECOND_VALUE'
_help_node_third_pattern_value='THIRD_VALUE'
_help_node_foot_pattern_value='FOOT_VALUE'

_help_node_title_pattern=r'<(?P<KEY>\w+)(.*)version=\"(?P<VERSION_NAME>\w[0-9])"(.*)name=\"(?P<TITLE>.*)\"'

_help_node_title_version_pattern=r'version(.*)name'

_help_node_b_pattern=r'<b>(?P<B_VALUE>.*)</b>'

_help_node_first_pattern=r'    ▪︎︎(?P<FIRST_VALUE>.*)'
_help_node_first_pattern_1 = r'   ︎︎︎︎ ▪︎︎(?P<FIRST_VALUE>.*)'
_help_node_first_pattern_2 = r'▪︎︎(?P<FIRST_VALUE>.*)'
_help_node_second_pattern=r'        ▫︎(?P<SECOND_VALUE>.*)'
_help_node_third_pattern=r'            ৹(?P<THIRD_VALUE>.*)'
_help_node_foot_pattern=r'^\</(?P<FOOT_VALUE>.*)>'

# 生成的excel文件每个语言包括key位于的表格位置 后面语言添加时需要在这里注明语言的位置
_sheet_title_key_location='A'
_sheet_title_zh_location='B'
_sheet_title_en_location='C'
_sheet_title_thai_location='D'
# 容错处理时标注的位置
_sheet_title_error_location='E'


_FILE_TYPE_ZH = 'zh'
_FILE_TYPE_EN = 'en'
_FILE_TYPE_THAI = 'thai'
