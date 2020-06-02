#if判断
# ==判断是否相等    =是赋值
# age=float(input("请输入你的年龄："))
# if age >=18:  #条件语句
#     print("成年人")
# else :
#     print("未成年人")

# a=1
# b=[2,3,1]
# if a in b:
#     print("a在b里面")
# else:
#     print("a不在b里面")


#for循环    遍历
# a=range(10)
# for b in a:
#     print(b)

# i={"name":"kk","age":15}
# for j in i:
#     print(j)
#     print(i.get(j))

#判断用户是否登录成功
# user=[{"username":"kk","password":"123456"}]
# zh=input("请输入你的账号：")
# mm=input("请输入你的密码：")
# for a in user:
#     if zh == a.get("username") and mm == a.get("password"):
#         print("{}登录成功".format(zh))
#     else :
#         print("登录失败")

#作业：判断账号密码是否对应。当这个账号存在时，就修改密码；当账号不存在时就新增一个账号
db = [{"username":"chenke", "password":"123456"},{"username":"zhangsan", "password":"123548"}]
zh=input("请输入账号：")
mm=input("请输入密码：")
count=1
for a in db:
    if zh == a.get("username"):
        a.update(password=mm)
        break  #跳出循环
    else:
        #a.update(username=zh,password=mm)
        # a["username"]=zh
        # a["password"]=mm
        #bug，当多个元素时，会多次添加
        if len(db) == count :
            db.append({"username":zh,"password":mm})
    count = count + 1       
print(db)