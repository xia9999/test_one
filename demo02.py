# age=int(input("请输入你的年龄："))
# if age==10:
#     print("要认真学习哦")
# elif age<16 and age>10:
#     print("一定要认真学习，不能说脏话")
# elif age<20:
#     print("可以慢慢规划未来的路线了，发现自己擅长的事，并且好好利用它")
# else :
#     print("不要感到迷茫，静心思考")


# a=input("请输入：")
# if a in '123456':
#     a=int(a)
#     print("谢谢")
# else :
#     print("请输入数字！")
#     exit()

# a=2.55
# if type(a) is str:
#     print("字符串")
# elif type(a) is int:
#     print("数字")
# elif type(a) is float:
#     print("小数")
# else :
#     print("啥也不是")

# a=2
# while a<5:
#     print("蜡笔小新")
#     a=a+1


# #练习：现需将十名学生的成绩录入系统，名字和成绩相对应，及格和不及格的同学分开存储
# jige={}
# bujige={}
# studentlist=("小新","哈哈","花花","小猫","小狗","你大爷","安然","安静")
# a=0
# while a<len(studentlist):
#     chengji=int(input("请输入"+studentlist[a]+"的成绩:"))
#     if chengji >=60:
#         jige[studentlist[a]]=chengji
#     else :
#         bujige[studentlist[a]]=chengji
#     a=a+1
# print("及格的学生及成绩:",jige)
# print("不及格的学生及成绩：",bujige)


#for循环
# a=(1,2,3,4,5,6,7,8,9)
# for i in a:
#     print(i)

# b=range(0,10,2)   #range数列生成器，这里生成[0,10)，中间间隔2的数列
# for i in b:
#     print(i)


# jige={}
# bujige={}
# studentlist=("小新","哈哈","花花","小猫","小狗","你大爷","安然","安静")
# for i in studentlist:
#     chengji=int(input("请输入"+i+"的成绩:"))
#     if chengji >=60:
#         jige[i]=chengji
#     else :
#         bujige[i]=chengji
# print("及格的学生及成绩:",jige)
# print("不及格的学生及成绩：",bujige)


#打印九九乘法表
# for a in range(1,10):
#     for b in range(1,a+1):
#         print(a,"x",b,"=",a*b,end="  ")
#     print()


"""
练习1：通过print打印，模拟一个红绿灯的功能，注意：红灯三十次，绿灯三十五次，黄灯三次。
练习2：
使用代码，实现一个注册功能，用户输入账号密码，
要求账号长度为5-8位，密码是6-12位，并且账号必须是小写开头。
存储到字典中，{username：password}
"""

# a=1
# while a > 0:
#     for i in range(0,30):
#         i="红灯"
#         print(i)
#     for e in range(0,35):
#         e="绿灯"
#         print(e)
#     for m in range(0,3):
#         m="黄灯"
#         print(m)

# light={"红灯":30,"绿灯":35,"黄灯":3}
# while True:
#     for i in light:
#         for j in range(light[i]):
#             print(i,j)

# username=input("请输入账号：")
# password=input("请输入密码：")
# if len(username)>=5 and len(username)<=8:
#     if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
#         if len(password)>=6 and len(password)<=12:
#             print("注册成功！",{username:password})
#         else:
#             print("请输入6-12位的密码！")
#     else:
#         print("账号必须以小写字母开头！")
# else:
#     print("请输入5-8位的账号！")


#自定义方法
"""
def 方法的声明 
方法名（参数）：
方法的说明
方法的逻辑代码
"""
# def jianfa(a,b):
#     """两数相减"""
#     if type(a) is int and type(b) is int:
#         print(a-b)
#     else :
#         print("请输入数字！")


def checkname(username):
    """
    校验用户名是否符合规范
    """
    if len(username)>5 and len(username)<8:
        if username[0] in "zxcvbnmasdfghjklopiuytrewq":
            return True
        else :
            return("请输入以小写字母开头的账号")
    else :
        return("请输入5-8位的账号！")

def checkpassword(password):
    """
    校验密码是否符合规范
    """
    if len(password)>6 and len(password)<12:
        return True
    else :
        return("请输入6-12位的密码！") 

username=input("请输入账号：")
password=input("请输入密码：")
if checkname(username)==True :
    if checkpassword(password)==True:
        print("注册成功!",{username:password})
    else :
        print("账号和密码不符合规范，请重新输入！")
else:
    print(checkname(username),checkpassword(password))
    