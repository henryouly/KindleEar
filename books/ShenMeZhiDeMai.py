#!/usr/bin/env python
# -*- coding:utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

from base import BaseFeedBook
from bs4 import BeautifulSoup

__author__ = 'henryouly'

def getBook():
    return ShenMeZhiDeMai

class ShenMeZhiDeMai(BaseFeedBook):
    title                 = u'什么值得买'
    description           = u'高性价比产品网购推荐'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    mastheadfile          = "mh_default.gif"
    coverfile             = "cv_default.jpg"
    oldest_article        = 1
    remove_attrs = ['class', 'style', 'id']
    remove_tags = ['embed']

    feeds = [ (u'经验盒子', 'http://jy.smzdm.com/feed', True) ]

    def postprocess(self, content):
        soup = BeautifulSoup(content, "lxml")
        for img in soup.find_all('img', attrs={'class':'face'}):
            img.decompose()
        for span in soup.find_all('span'):
            del span['card']
            del span['res-data-id']
        return unicode(soup)
