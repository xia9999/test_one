import pytest
import requests
from utils.filetools import read

def test_logout():
    token = read()    #获取token值
    url = "http://106.53.192.221:2333/logout"
    headers = {"Content-Type":"application/json","token":token}
    res = requests.get(url=url,headers=headers)
    print(res.text)
