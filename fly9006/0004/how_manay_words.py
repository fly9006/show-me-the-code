#!/usr/bin/env python
# -*- coding: utf8 -*-

import re


def how_manay_words(filename, word):
    """

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