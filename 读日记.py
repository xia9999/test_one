with open("D:/浪晋工具/日记.txt","r",encoding="utf-8") as b:
    text=b.readlines()    #readlines() 全部读取
for i in text:
    print(i)