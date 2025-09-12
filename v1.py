print(123)
print("Hello,world")
print(123+456)
print("Hello,Python")
print(123+456)
print("Hello,Python")
for i in range(1):
    print(i)
print("what is your name?")
name = input()
print("your name is " + name)
# python复数案例
a = 1 + 2j
print(a)
print(a.real)
print(a.imag)
# python特殊数据类型
# 列表
list1 = [1,2,3,4,5]
print(list1)
# 元组
tuple1 = (1,2,3,4,5)
print(tuple1)
# 字典
dict1 = {"name":"张三","age":18}
print(dict1)
# 集合
set1 = {1,2,3,4,5}
print(set1)
# python基础语法讲解
a = 1
b = 2
print(a+b)

print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)
# python运算符
# 算术运算符
# 赋值运算符
# 比较运算符
# 逻辑运算符
# 位运算符
# 成员运算符
# 身份运算符
# python流程控制
# 循环
for i in range(5):
    print(i)
# 跳转
while True:
    print("hello,world")
    break
# python函数
def print_hello():
    print("hello,world")
print_hello()
# python类
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_info(self):
        print("name is " + self.name)
        print("age is " + str(self.age))
    def print_hello(self):
        print("hello,world")
        print("my name is " + self.name)

person1 = Person("张三",18)
person1.print_info()
person1.print_hello()
    # python异常处理
try:
    print(1/0)
except Exception as e:
    print(e)
# python模块
import math
print(math.sqrt(16))
# python包
import sys
print(sys.path)
# python包管理
# python包管理工具 pip
# python包管理工具 pip3
# python包管理工具 pip3 install requests
# python包管理工具 pip3 uninstall requests
