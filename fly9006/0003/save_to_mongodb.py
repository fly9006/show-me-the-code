#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymongo
import traceback


def save_to_mongodb(code_list):
    """

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