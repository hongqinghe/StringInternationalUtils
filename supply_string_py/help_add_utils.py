import help_xml_constants as HC

import help_xml_parse_utils as H_UTILS

import help_excel_convert_xml

import help_xml_to_key_and_xml

import help_check_to_result

import string_tw_zh_convert

def toConvert():
    help_xml_to_key_and_xml.xmlParseToKeyValueXml()
    help_check_to_result.checkToResultXml()
    string_tw_zh_convert.helpToConvertTw()

if __name__ == "__main__":
    toConvert()
