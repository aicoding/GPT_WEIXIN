import re

#格式化日期工具函数
def date_convertion(date_string: str):
    #pattern1 = r"\b\d{4}-\d{2}-\d{2}\b"
    pattern1 = r"\b\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\b"
    pattern2 = r"\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\b"
    pattern3 = r"\b\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}\b"

    # 原始日期字符串
    #date_string = '2023-07-19 15:30:00'
    date_result = ''
    if re.search(pattern3, date_string):
        date_result = date_string
    elif re.search(pattern2, date_string):
        date_result = date_string + ".000"
    elif re.search(pattern1, date_string):
        date_result = date_string.replace(' ','T') + ".000"
    return date_result;