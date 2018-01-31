#!/usr/bin/env python
# -*- coding: utf8 -*-

import os


def exercise0011(file_name=''):
    """
    敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，
    则打印出 Freedom，否则打印出 Human Rights
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
            if words in lines:
                print 'Freedom \n'
            else:
                print 'Human Rights \n'

    return

if __name__ == '__main__':
    exercise0011(file_name='filtered_words.txt')
