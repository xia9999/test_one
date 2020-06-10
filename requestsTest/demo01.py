import requests
# #get请求
url="http://192.144.148.91:2333/get_title_img?num=3"    #接口信息
res = requests.get(url)    #发送请求并且获取返回值，res接收返回值
# print(res.text)      #打印返回值的信息

#post请求
u = "http://192.144.148.91:2333/login"    #接口信息
d = {"username":"anran","password":"123456789"}     #传的参数
res = requests.post(url=u,json=d)     #使用post方法向u接口请求，并且使用json格式的数据传参数
#print(res.text)    #打印返回值信息

# token要从登录之后来取
token = res.json()["data"]["token"]   # res.json()把返回值变成python的字典

#评论问题
u1 = "http://192.144.148.91:2333/comment/new"
d1 = {"ctype":1,"comment":"没抽空都没玩么我","fid":"3786"}
h1 = {"token":token}
res = requests.post(url=u1,json=d1,headers=h1)   # headers:请求头
#print(res.text)

#获取评论列表
u2 = "http://192.144.148.91:2333/getcomments"
d2 = {"ctype":1,"fid":"3786","pagenum":1}
res = requests.post(url=u2,json=d2)
#print(res.text)
cid = res.json()["data"]["contentlist"][0]["id"]  #获取评论id
# print(cid)
#修改评论
u2 = "http://192.144.148.91:2333/comment/update"
d2 = {"comment":"你洗漱看你飞而烦恼时","cid":cid}
res = requests.post(url=u2,json=d2,headers=h1)
#print(res.text)

res = requests.request("get",url=url)
print(res.text)