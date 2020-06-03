#方法，def 固定的       封装代码，代码的复用
#def 方法名(参数):
#return 返回值
#参数和返回值是可选的 ，参数和返回值可以是任意类型；参数可以有默认值
def sum(a,b):
    c=a+b
    return c
def test():
    print("heiheihei")
#返回多个值
def test1():
    return 10, 20, 30
a,b,c=test1()

i=4
j=10
m=sum(i,j)    #调用sum方法
print(m)
test()