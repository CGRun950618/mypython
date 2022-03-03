#定义函数一般三部分组成
# 函数名
# 函数参数
# 函数返回值
import functools


def hello(name):
    return name
my_new_name=hello('joke')
print(my_new_name)

# def greet():
#     print 'hello world'
# r=greet()
# print(r)

def add_one(x,y,z):
    return x+1,y+1,z+1
my_result=add_one(2,3,9)
print(my_result)

# 函数参数：
#         必须参数
#         默认参数
#         可变参数
#         关键字参数
# 默认参数要放在所有必选参数的后面 默认参数应该使用不可变对象
def add(x,y,z=1):  #x,y是必选参数 z默认参数
    return x + y + z
my_math=add(1,2)
print(my_math)

def my_new_add(*numbers):  #函数参数是可变的 参数前面加个*
    sum = 0
    for i in numbers:
        sum += i
    return sum
a=[1,2,3,4,5,7]
print(my_new_add(*a))


# 关键字参数则允许你将不定长度的键值对, 作为参数 传递给一个函数。
#   kwargs 可以接收不定长 度的键值对，在函数内部，它会表示成一个 dict
def add_1(**kwargs):
    return  kwargs
print(add_1(x=1,y=1))
# {'x': 1, 'y': 1}

# def func(x,y,z=0,*args,**kwargs):
#     print ('x=',x)
#     print ('y=',y)
#     print ('z=',z)
#     print ('args=',args)
#     print ('kwargs=',kwargs)
# b=func(1,2,3,4,5,6,7,u=8,v=9)
# print(b)
#

# 一个函数接收另一个函数作为参数，这种函 数称之为高阶函数（Higher-order Functions）
def func(g,arr):
    return [g(x) for x in arr]

def double(x):
    return 2*x
def square(x):
    return x*x
# arr1=func(double,[1,2,3,4])
# arr2=func(square,[1,2,3,4])
# print(arr1)
# print(arr2)

# map/reduce/filter 是 Python 中较为常用的内建高阶函数，它们为函数式编程提供了不少便 利
print(map(int,[1,2,3,4]))
# <map object at 0x000001C460AE3C70>返回迭代器
print(list(map(square,[1,2,3,4])))

funcs=[double,square]  #列表元素=是函数对象
value=list(map(lambda f:f(5),funcs))
print(value)

# 就是lambda表达式，第二个是要累计的序列，第三个是初始值
# from functools import reduce
def func(x,y):
    print(x,y)
functools.reduce(func,[1,2,3,4])

even_num=list(filter(lambda x:x%2==0,[1,2,3,4,5,6]))  #filter函数用于过滤
print(even_num)

 #关键字lambda是个匿名函数 ：前面变量是匿名函数的参数
#  lambda函数不能包含命令，包含的表达式不能超过一个
f=lambda x:2*x
my_new_1=f(8)
print(my_new_1)

# def func(g,arr):
#     return [g(x) for x in arr]
#
# def add_one(x):
#     return x+1
# arr=func(add_one,[1,2,3,4])
# print(arr)

arr=list(map(lambda x:x+1,[1,2,3]))
print(arr)

def sq(x):
    return x*x
value=list(map(sq,[y for y in range(10)]))
print(value)



