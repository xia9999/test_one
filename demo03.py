
# def checkusername(username,password):
#     if len(username)>5 and len(username)<9:
#         if username[0] in "qwertyuioplkjhgfdsazxcvbnm":
#             if len(password)>6 and len(password)<=12:
#                 if password[0] in "/+*-.@#$%^&":
#                     return "注册成功！"
#                 else :
#                     return "密码必须以特殊字符开头！"
#             else :
#                 return "请输入6-12位的密码！"
#         else :
#             return "请输入以小写字母开头的账号！"
#     else :
#         return "请输入5-8位的账号！"
# username=input("请输入账号：")
# password=input("请输入密码：")
# print(checkusername(username,password),{username:password})


"""
class  类的生明
类名的第一个字母必须大写
所有类的父类是object
所有方法都必须传一个叫self的参数  self指类本身
例如：def __init__ (self):  __init__是默认属性方法，接收参数
继承：class 类名 (需要继承的父类名):

"""
# class Test():
#     def __init__ (self):
#         self.name="张三"
#         self.sex="公"
#         self.age=3
#         self.yanse="白色"
#         self.pizhong="中华田园犬"
#     def caiyi (self,num):
#         print("你的名叫"+self.name+"的为"+self.sex+"的只有三岁的"+self.yanse+self.pizhong)
#         if num=="转圈":
#             print("开始转圈了")
#         if num=="跳跃":
#             print("开始跳跃了")

# zhangsan=Test()   #类的实例化
# zhangsan.caiyi("跳跃")   #方法的调用
# print(zhangsan.sex)

class BoyFirend():
    def __init__ (self,name,sex,age,shenggao,mingzhu):
        self.name=name
        self.sex=sex
        self.age=age
        self.shenggao=shenggao
        self.mingzhu=mingzhu
    def like (self,num):
        if num == 1:
            print("很喜欢打游戏")
        elif num == 2:
            print("喜欢看玄幻小说")
        elif num == 3:
            print("平时没事喜欢睡懒觉")
    def techang (slef):
        print("没有啥特长，腿特长")
people=BoyFirend("刘新","男",22,175,"汉族")
people.techang()
people.like(3)
class Stu(BoyFirend):
    def xuexi (slef):
        print("大傻傻子")
a = Stu("蜡笔小新","男",12,140,"大日本帝国")
a.xuexi()
print(a.name)
print(people.name)
        
