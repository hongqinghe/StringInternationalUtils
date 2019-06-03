from help_string import help_xml_to_key_and_xml, help_check_to_result

from normal_string import string_tw_zh_convert


def toConvert():
    help_xml_to_key_and_xml.xmlParseToKeyValueXml()
    help_check_to_result.checkToResultXml()
    string_tw_zh_convert.helpToConvertTw()

if __name__ == "__main__":
    toConvert()
