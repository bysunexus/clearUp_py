# -*- coding: utf-8 -*-
'''
Created on 2012-5-18

@author: ABC
'''

def transferCode(srcStr,fromCode,toCode):
    tmp = srcStr
    if not isinstance(srcStr, unicode):
        tmp = unicode(srcStr,fromCode)
    tmp = tmp.encode(toCode)
    return tmp