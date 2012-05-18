# -*- coding: utf-8 -*-
'''
Created on 2012-5-16

@author: ABC
'''
from org.bysun.apkreader.directory import FileListBuilder
from org.bysun.apkreader.file import ApkFileOperator

def process(path):
    builder = FileListBuilder(path,['apk'])
    apks = builder.listFile()
    operator = ApkFileOperator(path)
    operator.process(apks)

if __name__ == '__main__':
    path = 'D:\\apk_back\\'
    process(path)
