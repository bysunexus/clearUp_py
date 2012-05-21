# -*- coding: utf-8 -*-
'''
Created on 2012-5-10

@author: bysun
'''
import os
from org.bysun.apkreader.codeUtils import transferCode
class FileListBuilder(object):
    '''
    文件列表读取
    '''
    def __init__(self,basePath,filterStr):
        '''
        Constructor
        '''
        self.fileList = []
        self.basePath = basePath
        self.filter = filterStr
        self.__buildListFile()
        
    def __validBasePath(self):
        '''
        判断是否是已存在目录
        '''
        if os.path.exists(self.basePath) & os.path.isdir(self.basePath):
            return True
        else:
            return False
        
    def __buildListFile(self):
        '''创建文件列表'''
        if self.__validBasePath():
            for fs in os.walk(self.basePath):
                for f in fs[2]:
                    extName = os.path.splitext(f)[1][1:];
                    if extName in self.filter:
                        self.fileList.append(transferCode(os.path.join(fs[0],f), 'gbk', 'utf-8'))
                        
    def listFile(self):
        '''返回文件列表'''
        return self.fileList
    def getBasePath(self):
        '''返回基础目录路径'''
        return self.basePath

