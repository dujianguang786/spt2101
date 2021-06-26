"""
  程序执行的顺序:
    1.从上到下
    2.从右往左
    3.有小括号先执行小括号里面的代码
  运算符优先级从高到低的顺序：
     或<与<非<赋值<比较<加、减<乘、除、取余、取整<安位取反~<幂** 
   审题思路：
     1、先确定要实现的操作/功能
     2、进行操作的实现
     3、对不正确操作/bug进行处理
"""
from pymysql import *

# 建立连接

# con = connect(host='127.0.0.1', port=3306, database='demo7',
#               user='root', password='123', charset='utf8')
con = connect(host="127.0.0.1", port=3306, user="root",
              password="123", database="demo", charset="utf8")
print(con)

# 创建游标
ret = con.cursor()
str = 'insert into student VALUES ("7","明达",36,"datong", "md")'
# execute方法用于增删改操作，返回值受影响的行数
res = ret.execute(str)

# 提交操作
con.commit()
print(res)

# 关闭游标
ret.close()
# 关闭连接
con.close()
