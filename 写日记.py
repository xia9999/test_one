# import time   #导包
# now=time.strftime("%y-%m-%d %H:%M:%S")   #获取当前时间
# text=input("请输入：")
# with open("D:\浪晋工具\日记.txt","a",encoding="utf-8") as a:
#     a.write(now+"\n")
#     a.write(text+"\n")
#     a.write("++++++++++++++++++++++++++++++"+"\n")
    
# import time
# now =time.strftime("%y-%m-%d %H:%M:%S")
# a=input("请输入：")
# with open("D:\浪晋工具\写日记2.txt","a",encoding="utf8") as b:
#        b.write(now+"\n")
#        b.write(a+"\n")

with open("D:\浪晋工具\写日记2.txt","r",encoding="utf8") as a:
    b=a.readlines()
    for c in b:
        print(c)

