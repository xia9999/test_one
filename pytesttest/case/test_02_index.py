import pytest
import requests
import os,sys
sys.path.append(os.getcwd())
from utils.dbtools import select 

def test_01_title_img():
    """
    查看轮播图测试用例，不传参
    """
    url = "http://106.53.192.221:2333/get_title_img"
    res = requests.get(url=url)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    sql = "select * from t_title_img"
    assert len(select(sql)) !=0

def test_02_getcoures():
    """
    获取推荐教程，传参pagenum=1,一页最多返回10条数据
    """
    url1 = "http://106.53.192.221:2333/getcoures?pagenum=1"
    res = requests.get(url=url1)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["data"]["counts"] <= 10
    sql = "select * from t_coures"
    assert len(select(sql)) != 0
   

def test_03_getcoures():
    """
    获取推荐教程，不传参，默认返回三条数据
    """
    url1 = "http://106.53.192.221:2333/getcoures?pagenum=1"
    res = requests.get(url=url1)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    assert res.json()["data"]["counts"] != 3
    sql = "select * from t_coures"
    assert len(select(sql)) != 0

def test_04_getcoures():
    """
    获取教程详情
    """   
    url = "http://106.53.192.221:2333/getcoures?cid=132"
    res = requests.get(url=url)
    assert res.status_code == 200
    assert res.json()["status"] == 200
    sql = "select * from t_coures where id = 132"
    assert len(select(sql)) != 0