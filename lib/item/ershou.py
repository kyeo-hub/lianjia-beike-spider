#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 二手房信息的数据结构


class ErShou(object):
    def __init__(self, district, area, community_name, name, price, unitprice, desc, pic):
        self.district = district
        self.area = area
        self.community_name= community_name
        self.price = price
        self.unitprice = unitprice
        self.name = name
        self.desc = desc
        self.pic = pic

    def text(self):
        return self.district + ";" + \
            self.area + ";" + \
            self.name + ";" + \
            self.community_name + ";" + \
            self.price + ";" + \
            self.unitprice + ";" + \
            self.desc + ";" + \
            self.pic
