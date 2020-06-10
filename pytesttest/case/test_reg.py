import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
from utils.dbtools import commit,select


# def test_01_reg():
#     """
#     正确注册账号测试用例
#     """
#     url = "http://106.53.192.221:2333/regist"
#     data = {"username":"shazii","password":"123456789","phone":"15159245154","email":"8666@qq.com"}
#     res = requests.post(url=url,json=data)  #使用post方法向u接口请求，并且使用json格式的数据传参数
#     print(res.text)
#     assert res.status_code == 200
#     assert res.json()["status"] == 200
#     sql = "select * from t_user where username='{}'".format(data.get("username"))
#     assert len(select(sql)) !=0

# def test_02_reg():
#     """
#     用户名已存在注册
#     """
#     url = "http://106.53.192.221:2333/regist"
#     data1 = {"username":"shazi","password":"123456789","phone":"15154585324","email":"86@qq.com"}
#     res = requests.post(url=url,json=data1)
#     assert res.status_code == 200
#     assert res.json()["status"] != 200
#     sql = "select * from t_user where username = '{}'".format(data1.get("username"))
#     assert len(select(sql)) != 0


# def test_03_reg():
#     """
#     使用已注册的手机号注册
#     """     
#     url = "http://106.53.192.221:2333/regist"
#     data2 = {"username":"shazi1","password":"123456789","phone":"15154581323","email":"886@qq.com"}
#     res = requests.post(url=url,json=data2)
#     print (res.text)
#     assert res.status_code == 200
#     assert res.json()["status"] != 200
#     sql = "select * from t_user where phone = '{}'".format(data2.get("phone"))
#     assert len(select(sql)) != 0
#     print (res.text)


# def test_04_reg():
#     """
#     使用已绑定的邮箱注册
#     """
#     url = "http://106.53.192.221:2333/regist"
#     data3 = {"username":"shazi2","password":"123456789","phone":"15145824975","email":"866@qq.com"}
#     res = requests.post(url=url,json=data3)
#     assert res.status_code == 200
#     assert res.json()["status"] != 200
#     sql = "select * from t_user where email = '{}'".format(data3.get("email"))
#     assert len(select(sql)) != 0
#     print(res.text)
    
