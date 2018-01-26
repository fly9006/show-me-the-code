#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import re


def exercise0006(dir_path=''):
    """
    你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，
    请统计出你认为每篇日记最重要的词。
    :return:
    """

    file_list = os.listdir(dir_path)
    for filename in file_list:
        print 'current file is {0} \n'.format(filename,)
        word_list = []
        split_file_list = str(filename).split('.')
        if split_file_list[-1] != 'txt':
            continue
        cur_file_path = os.path.join(dir_path, filename)
        with open(cur_file_path, 'r+') as f:
            lines = f.readlines()
            for line in lines:
                line_data_list = line.split(' ')
                for word_data in line_data_list:
                    r = re.match(pattern='^[A-Za-z]*', string=word_data)
                    word_list.append(str(r.group()).lower().strip())
        for word in set(word_list):
            print '''the word is {0}, count number is {1}
                   '''.format(word, word_list.count(word))
    return

if __name__ == '__main__':
    exercise0006(dir_path='.')
