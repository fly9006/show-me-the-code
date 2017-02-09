#!/usr/bin/env python
# -*- coding: utf8 -*-

from PIL import Image, ImageDraw, ImageFont


def add_red_num(avatar):
    """
    将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
    :return:
    """
    width, height = avatar.size
    NumWidth = width/5

    draw = ImageDraw.Draw(avatar)
    NumFont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=60)
    draw.text((width-NumWidth, 0), '3', fill=(256, 0, 0), font=NumFont)

    avatar.save('./new_iverson.jpg')
    avatar.show()


if __name__ == '__main__':
    avatar = Image.open('iverson.jpg')
    add_red_num(avatar)
