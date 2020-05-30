# print("你好"+'哈哈哈哈')
# print(22)
# print(2.333)
# print(5>9)
# print((2,3,4))
# print([3,5,4])
# print({"fd","dd"})

# a=float(input("请输入："))
# b=float(input("请再次输入："))
# print("获取到的值：",a+b)

# a=str("我是谁")
# b=int(2333)
# c=float(2.3362)
# d=tuple((2,5,3,6))
# e=list([1,2,3,5])

# print("获取到的字符串的长度：",len(a))
# print("获取元组的长度：",len(d))
# print("获取数组的长度：",len(e))


# a=5
# print(type(a))

# a=input("请输入：")
# b=input("请输入：")
# print("获取到的内容：",a+b)
# print("获取到的字符长度：",len(a+b))

# a=(2,4,3,5,6,4,4,4,4)
# print(a[2])   #获取下标为2的值，下标是从零开始编号的，不会重复
# print(a.index(6))   #获取6的下标
# print(a.count(4))   #统计4的个数
# print(a[2:4])    #切片，下标2到4的值，批量输出元组的值。左闭右开
# print(a[-1])    #下标也可以从右边开始数，-1，-2，-3.......
# print(a.count(a.index(3)))    
# print(a[a.index(2):a.index(5)])

# a=[2,4,5,6,3,5,4]    #定义一个数组
# print(a[2])    #输出下标为2的值
# print(a.index(4))   #输出值为4的下标，就近原则
# print(a.count(4))   #统计值为4的个数
# a.append("你是猪")   #往数组中追加数据，在最后一位
# print(a) 
# a.insert(1,"你还是猪")    #在下标为1的位置上添加值为你还是猪的数据
# print(a)
# b=list(a.pop(a.index("你是猪")))    #pop() 剪切数据，将一个值从一个变量中拿出来，再赋值给另一个变量
# print(b)
# b.clear()   #清空数据
# print(a,b)
# b.extend(a)   #合并数组
# print(b)
# b.remove(2)   #删除值为2的数据
# print(b)

#字典的特点：1.字典中的值没有顺序。2.字典中的值必须是以键值对的形式存在，key:value
# a={"姓名":"蜡笔小新","年龄":20,"性别":"男"}   #定义一个字典
# print(a["姓名"])    #取值key为姓名的值
# a["爱好"]="睡觉"    #添加一个key为爱好的值为睡觉
# print(a)
# a["年龄"]=18   #修改key为年龄的值为18
# print(a)
# print(a.get("姓名"))  #获取key为姓名的值
# b=a.pop("爱好")    #将爱好的值剪切给变量b
# print(a,b)
# a.update(性别='女')   #修改性别的值为女
# a.update(特长='腿特长')    #新增一个key为特长，值为腿特长的值
# print(a)


#练习 ：获取用户输入的个人信息，并且存储到字典中，个人信息：name，age，sex
# b=input("请输入姓名：")
# c=input("请输入你的年龄：")
# d=input("请输入你的性别：")
# a={"name":b,"age":c,"sex":d}
# print(a)

# a = input("请输入：")
# b = len(a)
# print("输入的字符长度：",b)

