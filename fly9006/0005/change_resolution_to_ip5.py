#!/usr/bin/env python
# -*- coding: utf8 -*-

from PIL import Image
import os


def change_resolution_to_ip5(dirname):
    """
    你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
    :param imgfile:
    :return:
    """
    for parent, dirnames, filename in os.walk(dirname):
        if len(filename) > 0:
            for imgfile in filename:
                img = Image.open(os.path.join(os.getcwd(), dirname, imgfile))
                (x, y) = img.size
                new_x = 1136
                new_y = y * new_x/x
                img.resize((new_x, new_y), Image.ANTIALIAS)
                new_img_name = imgfile.split('.')[0] + '-for-ip5' + '.' + imgfile.split('.')[1]
                img.save('./img/%s' % new_img_name)
    return

if __name__ == '__main__':
    change_resolution_to_ip5('img')