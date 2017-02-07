#!/usr/bin/env python
# -*- coding: utf8 -*-

import string
from random import choice


def create_random_string():
    """

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
