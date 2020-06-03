import pymysql

def select(sql):
    """
     查询数据；只能查询，不能修改，删除，新增数据
    """
    #连接数据库
    db=pymysql.connect(host="127.0.0.1",user="root",password="123456",db="test")
    #获取游标:打开查询窗口
    cur=db.cursor()
    #执行SQL语句
    cur.execute(sql)
    #得到执行的结果
    res=cur.fetchall()
    #关闭数据库
    db.close()
    return res

# sql="select * from students where sid =25"
# a=select(sql)
# print(a)
# print(len(a))

def commit(sql):
    """
     修改，删除，新增数据，不能传select
    """
    #连接数据库
    db=pymysql.connect(host="127.0.0.1",user="root",password="123456",db="test")
    #获取游标:打开查询窗口
    cur=db.cursor()
    #执行SQL语句
    cur.execute(sql)
    #提交修改
    db.commit()
    #关闭数据库
    db.close()
    return True
#sql="update students set sname='小屁孩' where sid=1"
#sql="insert into students(sid,sname,tel,sex) values(33,'灰姑凉',123456789,'女')"
# sql="delete from students where sid =22"
# commit(sql)