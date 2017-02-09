#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymongo
import traceback


def save_to_mongodb(code_list):
    """
    将 0001 题生成的 200 个激活码（或者优惠券）保存到 mongo 非关系型数据库中。
    :return:
    """

    conn = pymongo.MongoClient(host='', port='', username='', password='')
    code_db = conn['code_db']
    code_doc = code_db.create_collection('code_col')

    for code in code_list:
        try:
            code_doc.insert_one({'code': code})
        except Exception, e:
            print traceback.format_exc()
            continue
    return


if __name__ == '__main__':
    save_to_mongodb(code_list=[])