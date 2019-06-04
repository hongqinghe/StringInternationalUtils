from help_string import help_xml_to_key_and_xml, help_check_to_result

from normal_string import string_tw_zh_convert
from base_lib import LanuageConvertUtils as LANG
from help_string import help_xml_constants as HC


def toConvert():
    help_xml_to_key_and_xml.xmlParseToKeyValueXml()
    help_check_to_result.checkToResultXml()
    LANG.convert_zh_to_tw(HC._SOURCE_ZH_PATH, HC._SOURCE_TW_PATH)
    # string_tw_zh_convert.helpToConvertTw()


if __name__ == "__main__":
    toConvert()
