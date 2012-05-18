# -*- coding: utf-8 -*-
from distutils.core import setup 
import py2exe

includes = ['org']

options = {"py2exe": 
            {   "compressed": 1,
                "optimize": 2,
                "includes": includes,
                "bundle_files": 1,
                "packages": ['org']
            } 
          } 
setup(
    version="0.1.0",
    description="apl cleanup",
    name="cleanup",
    options=options,
    zipfile=None,
    windows=[{"script": "D:\\workspase\\my\\clearup\\src\\org\\bysun\\apkreader\\GUIMain.py"}],
    ) 
