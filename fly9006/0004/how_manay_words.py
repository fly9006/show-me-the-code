#!/usr/bin/env python
# -*- coding: utf8 -*-

import re


def how_manay_words(filename, word):
    """
    任一个英文的纯文本文件，统计其中的单词出现的个数。
    :return:
    """
    count = 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            p = '\s(%s)(\s|\.|,|;|\?|!|\')' % (word, )
            res = re.findall(re.compile(p), line)
            count += len(res)
            if res:
                print res
    print "how manay words: %s" % (count, )


if __name__ == '__main__':
    how_manay_words('test.txt', 'Relations')