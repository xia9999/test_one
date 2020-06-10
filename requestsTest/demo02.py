import requests
from dbtools import select

url="http://192.144.148.91:2333/login"    #接口信息
data = {"username":"anran","password":"123456789"}
res = requests.post(url=url,json=data)
print(res.status_code)
#断言，判断
assert res.status_code == 200        #http状态码
assert res.json()["status"] == 200   #结果码

sql = "select * from t_user where username='{}'".format(data.get("username"))
if len(select(sql)) != 0:
    print("测试通过")
else:
    print("测试失败")