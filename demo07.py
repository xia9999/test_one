from dbtools import select 
from dbtools import commit
#验证登录账号是否成功=============================================
username = input("请输入账号：")
password = input("请输入密码：")
sql="select * from students where sname='{}' and num='{}'".format(username,password)
res = select(sql)
if len(res) != 0 :
    print("登陆成功")
else:
    print("登录失败！")

#注册账号========================================================
# username = input("请输入账号：")
# password = input("请输入密码：")
# sql="insert into students(sname,num) values('{}',{})".format(username,password)
# res = commit(sql)
# if res == True:
#     sql= "select * from students where sname='{}' and num='{}'".format(username,password)
#     res =select(sql)
#     if len(res) != 0:
#         print("注册成功") 
# else:
#     print("注册失败！")
#================================================================
#注册账号，判断数据库中是否已存在该账号，如果已存在，则提示该账号已存在，请直接登录
# username = input("请输入账号：")
# password = input("请输入密码：")
# sql= "select * from students where sname='{}'".format(username)
# res = select(sql)
# if len(res) == 0:
#     sql="insert into students(sname,num) values('{}',{})".format(username,password)
#     res = commit(sql)
#     print("注册成功")
# else:
#     print("该账号已存在，请直接登录！")