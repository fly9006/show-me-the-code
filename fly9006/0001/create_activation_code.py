#!/usr/bin/env python
# -*- coding: utf8 -*-

import string
from random import choice


def create_random_string():
    """
    做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
    :return:
    """
    code = ''
    for y in range(20):
        random_source = string.digits + string.lowercase
        code += choice([z for z in random_source])
    code = code.upper()
    return code


def create_activation_code():
    """

    :return:
    """
    result = []
    for x in range(200):
        code = create_random_string()
        while code in result:
            code = create_random_string()
        result.append(code)

    return result


if __name__ == '__main__':
    print create_activation_code()
