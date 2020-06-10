import pytest
import requests
import os, sys
sys.path.append(os.getcwd())    #跨域连接文件
from utils.dbtools import select   
from utils.filetools import save

def test_01_login():
    """
    登录成功的测试用例
    """
    u = "http://106.53.192.221:2333/login"
    d = {"username":"anran", "password":"123456789"}
    res = requests.post(url=u,json=d)
    #assert 断言，判断
    assert res.status_code ==200   #http状态码
    assert res.json()["status"] == 200    #结果码

    sql = "select * from t_user where username='{}'".format(d.get("username"))
    assert len(select(sql)) !=0
    save(res)    #保存token值
    token = res.json()["data"]["token"]
    print(token)
