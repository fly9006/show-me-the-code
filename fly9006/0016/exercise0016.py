#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import json
import tablib


def exercise0016(file_name=''):
    """
    纯文本文件 numbers.txt, 将里面的内容写到 numbers.xls 文件中
    :return:
    """

    str_data = ''
    excel_data = []
    file_path = os.path.join(os.curdir, file_name)
    if not os.path.exists(file_path):
        return 'Error'
    with open(file_path, 'r+') as f:
        for x in f.readlines():
            str_data += str(x).strip()
    try:
        data2 = json.loads(str_data)
    except:
        return 'Error'
    for n in data2:
        if isinstance(n, list):
            excel_data.append(n)
    sheet_data = tablib.Dataset(*excel_data, headers=())
    with open('numbers.xls', 'wb') as f:
        f.write(sheet_data.xls)

    return

if __name__ == '__main__':
    exercise0016(file_name='numbers.txt')
