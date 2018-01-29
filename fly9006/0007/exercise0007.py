#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import re


def exercise0007(dir_path=''):
    """
    有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
    包括空行和注释，但是要分别列出来。
    :return:
    """

    available_extension_list = ['py']
    file_list = os.listdir(dir_path)
    pattern1 = re.compile('^\s*#+.*')  # #注释
    pattern2 = re.compile('^\s*("""|\'\'\')+')  # 连续三个引号注释

    for filename in file_list:
        print 'current directory is {0}'.format(os.path.abspath(os.curdir),)
        print 'current file is {0}'.format(filename,)
        total_line_count = 0
        total_blank_line_count = 0
        total_code_line_count = 0
        total_comments_line_count = 0
        comments_index_list = []
        split_file_list = str(filename).rsplit('.')
        extension_name = split_file_list[-1]
        if extension_name not in available_extension_list:
            continue

        cur_file_path = os.path.join(dir_path, filename)
        with open(cur_file_path, 'r+') as f:
            lines = f.readlines()
            for index in range(len(lines)):
                line = lines[index]
                total_line_count += 1
                if line in ['', ' ', '\n']:
                    total_blank_line_count += 1
                    continue

                r1 = pattern1.match(line)
                if r1:
                    total_comments_line_count += 1
                    continue
                r2 = pattern2.match(line)
                if r2:
                    comments_index_list.append(index)
                    if len(comments_index_list) % 2 == 0:
                        total_comments_line_count += (
                            comments_index_list[1] - comments_index_list[0] + 1)
                        comments_index_list = []
                    continue
                total_code_line_count += 1

        print 'total_blank_line_count is: {0}'.format(total_blank_line_count,)
        print 'total_line_count is: {0}'.format(total_line_count,)
        print 'total_code_line_count is: {0}'.format(total_code_line_count,)
        print '''total_comments_line_count is: {0}
                '''.format(total_comments_line_count,)
    return

if __name__ == '__main__':
    exercise0007(dir_path=os.curdir)
