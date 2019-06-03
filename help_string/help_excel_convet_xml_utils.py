from help_string import help_xml_to_key_and_xml, help_check_to_result, help_excel_convert_xml


def toConvert():
    help_excel_convert_xml.excleConversionXml()
    help_xml_to_key_and_xml.xmlParseToKeyValueXml()
    help_check_to_result.checkToResultXml()

if __name__ == "__main__":
    toConvert()