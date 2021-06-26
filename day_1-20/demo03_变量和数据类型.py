#变量命名法
#1.驼峰命名法
FirstName = "张三"  #大驼峰
firstName = "李四"  #小驼峰
print(FirstName,firstName)

#2.下划线命名法
first_name = "王五"
print(first_name)


#变量
number1= 10  #先声明变量，再给变量赋值
print(number1,id(number1))

number2= 10
print(number2,id(number2))
#变量赋值写法1、
number1 = 40
print(number1,id(number1))
#变量赋值写法2、
number1 = number2 = 30
#变量赋值写法3、
name ,age ,sex = "张三" ,20 ,"男"
print(name,age,sex,type(name),type(age),type(sex))

