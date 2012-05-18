# -*- coding: utf-8 -*-
'''
Created on 2012-5-10

@author: bysun
'''

class ApkInfoDto(object):
    ''' APK文件信息 '''
    def __init__(self):
        '''
        Constructor
        '''
        self.name = None
        self.pkgName = None
        self.version = -1
        self.versionCode = None
        self.cnName = None
        self.apkFile = None