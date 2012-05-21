# -*- coding: utf-8 -*-
'''
Created on 2012-5-14
'''
import os
import re

from org.bysun.apkreader.model import ApkInfoDto
from org.bysun.apkreader.codeUtils import transferCode

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
            info = self.__readApkInfo(apk)
            # 未读取到信息 继续
            if not bool(info.pkgName) or info.version == -1:
                continue
            #处理文件
            self.__processFile(info)
            
    def __processFile(self,info):
        '''
        处理apk文件
        '''
        if not self.versions.has_key(info.pkgName):
            self.versions[info.pkgName] = info
            self.__renameFile(info);
        else:
            old = self.versions.get(info.pkgName)
            if info.version>old.version:
                #删除旧文件
                self.__deleteFile(old)
                #改名新文件
                self.__renameFile(info)
                #放入新版本信息
                self.versions[info.pkgName] = info
            else:
                #删除读取到的文件
                self.__deleteFile(info)
            
    def __renameFile(self,info):
        fromFile = transferCode(info.apkFile, 'utf-8', 'gbk')
        toFile = transferCode(self.__buildFileName(info), 'utf-8', 'gbk')
        os.rename(fromFile, toFile)
        info.apkFile = self.__buildFileName(info)
    
    def __deleteFile(self,info):
        fileName = transferCode(self.__buildFileName(info), 'utf-8', 'gbk')
        os.remove(fileName)
        
    def __buildFileName(self,info):
        return self.baseFilePath+info.cnName+'_'+str(info.version)+'.apk'
        
    def __readApkInfo(self,apk):
        '''
        读取并返回apk信息
        @return: ApkInfoDto
        '''
        info = ApkInfoDto()
        # 取得文件名
        info.name = os.path.splitext(apk)[0]
        info.apkFile = apk
        cmd = transferCode(os.getcwd()+os.sep+'aapt.exe dump badging "'+apk+'"','utf-8','gbk')        
        for lineStr in os.popen(cmd).readlines():
            if lineStr.startswith("package: name='") :
                infos = re.match(r"package: name='(.*?)' versionCode='(.*?)' versionName='(.*?)'", lineStr).groups()
                info.pkgName = infos[0]
                info.version = int(infos[1])
                info.versionCode = infos[2]
            elif lineStr.startswith("application: label='") :
                infos = re.match(r"application: label='(.*?)' icon='.*?'", lineStr).groups()
                info.cnName = infos[0]
        return info