#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import re


def exercise0012(file_name=''):
    """
    敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，
    则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
    :return:
    """

    file_path = os.path.join(os.curdir, file_name)
    if not os.path.exists(file_path):
        return 'Error'
    while True:
        raw_data = raw_input('PLEASE INPUT SOME WORDS: ')
        words = str(raw_data).strip().decode('utf-8')
        with open(file_path, 'r+') as f:
            lines = [str(n).strip().decode('utf-8') for n in f.readlines()]
            for n in lines:
                words = words.replace(n, '*' * len(n)) if n in words else words
            print words

    return

if __name__ == '__main__':
    exercise0012(file_name='filtered_words.txt')
