#!/usr/bin/env python
# -*- coding: utf8 -*-

import pymysql


def save_to_mysql(code_list):
    """

    :return:
    """
    conn = pymysql.connect(host='', port='', user='', password='', database='')
    # 游标
    cursor = conn.cursor()

    # 创建表
    sql = """
            CREATE TABLE CODE(
                id int PRIMARY
                code VARCHAR UNIQUE
            )"""
    try:
        cursor.execute(sql)
    except Exception, e:
        conn.rollback()

    # 将优惠码轮询插入表
    for code in code_list:
        insert_sql = "INSERT INTO CODE(code,) VALUES (%s,))" % (code, )
        try:
            cursor.execute(insert_sql)
        except Exception, e:
            conn.rollback()

    cursor.close()
    return


if __name__ == '__main__':
    save_to_mysql(code_list=[])