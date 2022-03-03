from math import  pow
def make_pow(n):
    def inner_func(x):
        return  pow(x,n)
    return inner_func
pow2=make_pow(2)
print(pow2(6))
# 闭包的最大特点就是引用了自由变量，即使生成闭包的环境已经释放，闭包还是存在
# pow()函数方法 pow(x, y[, z])如果 z 在存在，则再对结果进行取模，其结果等效于 pow(x,y) %z

from math import  sqrt
class point(object):
    def __init__(self,x,y):
        self.x,self.y=x,y

    def get_distance(self,u,v):
        distance=sqrt((self.x-u)**2+(self.y-v)**2)
        return distance
pt=point(7,2)
value=pt.get_distance(10,6)
print(value)

def point(x,y):
    def get_distance(u,v):
        return sqrt((x-u)**2+(y-v)**2)
    return get_distance
pt=point(7,2)
value_1=pt(10,6)
print(value_1)


# 可以动态修改函数（或类）功能的函数就是装饰器。本质上，它是一个高阶函数
def info(value):
    def decorator(func):
        def wrapper(*args,**kwargs):
            print(value)
            return func(*args,**kwargs)
        return wrapper
    return decorator
@info('456')
def say_hello():
    print('同学你哦哦')
say_hello()


print(say_hello.__name__)

# def 炼丹炉(func): # func就是‘孙悟空’这个函数
#   def 变身(*args, **kwargs): #*args, **kwargs就是‘孙悟空’的参数列表，这里的‘孙悟空’函数没有传参数，我们写上也不影响，建议都写上
#       print('有火眼金睛了') # 加特效，增加新功能，比如孙悟空的进了炼丹炉后，有了火眼金睛技能
#       return func(*args, **kwargs) #保留原来的功能，原来孙悟空的技能，如吃桃子
#   return 变身 # 炼丹成功，更强大的，有了火眼金睛技能的孙悟空出世
#
# @炼丹炉
# def 孙悟空():
#   print('吃桃子')
#
# 孙悟空()
# # 输出:
# # 有火眼金睛了
# # 吃桃子
#

def derma(func):
        def color(*args,**kwargs):
            print('yellow')
            return func(*args,**kwargs)
        return color
def dragon_Place(x):
        def stick(*args,**kwargs):
            print('棍子')
            return x(*args,**kwargs)
        return stick
def monkey():
    print('吃桃子')
monkey()

# 闭包理解为一种特殊的函数，这种函数由两个函数的嵌套组成，且称之为外函数和内函数，外函数返回值是内函数的引用，此时就构成了闭包。
# 外层函数中的参数，不一定要有，据情况而定，但是一般情况下都会有并在内函数中使用到
# @a 就是将 b 传递给 a()，并返回新的 b = a(b)

def funcs(a,b):              #def 外层函数(参数):
    def line(x):               # def 内层函数():
        return  a*x-b               #  print('内层函数',参数)
    return line                  #return 内层函数
line=funcs(2,3)               #内层函数的引用=外层函数('传入参数')
print(line(5))                #内层函数的引用()


# 装饰器函数的本质是闭包函数
def canyou(func):
    def decorator(*args,**kwargs):
        if userAge>1 and userAge<10:
            return  func(*args,**kwargs)
        print('你年龄不适合')
    return decorator
@canyou
def play():
    print('开始播放动画片')
userAge=5
play()


# 1.闭包传参
def foo():
    num=1
    def add(n):
        nonlocal num
        num+=n
        return num
    return add
f=foo()
print(f(2))

def pig():
    a=4
    def add(n):
        a=n+4
        return a
    return add
p=pig()
print(p(3))


#functools.partial(func[,*args][, **kwargs])
def multiply(x,y=3):
      return x*y
print(multiply(2))
#固定函数参数，返回一个新的函



