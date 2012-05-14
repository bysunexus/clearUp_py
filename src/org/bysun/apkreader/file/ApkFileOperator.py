# -*- coding: UTF-8 -*-
'''
Created on 2012-5-14
'''
import os
import re

from org.bysun.apkreader.model.ApkInfoDto import ApkInfoDto
class ApkFileOperator(object):
    '''
    APK 文件操作
    '''
    versions = {}
    files = {}

    def __init__(self,baseFilePath):
        self.baseFilePath = baseFilePath
        
    def process(self,apks):
        '''
        处理apk文件
        '''
        # 循环apk并处理
        for apk in apks:
            # 读取文件信息
            info = self.readApkInfo(apk)
            # 未读取到信息 继续
            if bool(info.pkgName) or info.version == -1:
                continue
            #处理文件
            
            
    def processFile(self,apk,info):
        '''
        处理apk文件
        @param apk:string 
        @param info: ApkInfoDto
        '''
        vson = self.versions.get(info.pkgName)
        
                
    def readApkInfo(self,apk):
        '''
        读取并返回apk信息
        @return: ApkInfoDto
        '''
        info = ApkInfoDto()
        # 取得文件名
        info.name = os.path.splitext(apk)[0]
        cmd = 'aapt.exe dump badging "'+apk+'"'
        for lineStr in os.popen(cmd).readlines():
            if lineStr.startswith("package: name='") :
                infos = re.match(r"package: name='(.*?)' versionCode='(.*?)' versionName='(.*?)'", lineStr).groups()
                info.pkgName = infos[0]
                info.version = int(infos[1])
                info.versionCode = info[2]
            elif lineStr.startswith("application: label='") :
                infos = re.match(r"application: label='(.*?)' icon='.*?'", lineStr).groups()
                info.cnName = infos[0]
        return info