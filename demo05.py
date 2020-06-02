import time     #python自带的包
import sys
import unittest

from test.one import a   #导入自定义包


try:
    i=a
    if type(i) is str:
        print(22)
except:
    print(i)

