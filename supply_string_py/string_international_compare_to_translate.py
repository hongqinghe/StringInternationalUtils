# 国际化版本 查找出未翻译的 并在主干上查找替换翻译

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os
import new_business_to_add_xml as ADD

import check_basic_zh_other_xml_correct as CHECK
import string_xml_constants as SC
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, ElementTree
import string_tw_zh_convert as ZW
