# 第一个缺点就是运行速度慢，和 C 程序相比非常慢，因为 Python 是解释型语言
# 第二个缺点就是代码不能加密

# name=input('请输入姓名：')
# print('你的姓名:'+name)

# 字符串内部  既包含’又包含‘可以用转义字符\
print('sex\t+baby'+r'\\\sexbay...'+'''line
line2
line3''')  #r默认不转义  '''...'''程序省略后面3个点

# 布尔值
print(3<2 or 3>1)  #一个布尔值只有True False

print(10//3)  #//只取整数部分

print(ord('a'))  #ord函数获取字符的整数
print(chr(66))  #编码转对应字符

# %d 整数  如果只有一个%?，括号可以省略。格式化
# %f 浮点数
# %s 字符串
# %x 十六进制整数

print('hello,%s'%  'world')
print('hi %s ,you have $%d.'%('Michael',10000))
print('you is %s'%'sb')
# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转 义，用%%来表示一个%：

s1=72
s2=85
r=(s1-s2)/72
print('%f'%r)

# 只有 1 个元素的 tuple 定义时必须加一个逗号,
t1=(1,)
print(t1)

L = [
 ['Apple', 'Google', 'Microsoft'],
 ['Java', 'Python', 'Ruby', 'PHP'],
 ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(len(L[1]))

# if语句从上到下判断，第一个判断True的话就不再执行elif和else

sum=0
for x in range(101):
    sum=sum+x
print(sum)

sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
print(sum)

for x in L[1]:
     print('hello,'+x)

# 和 list 比较，dict 有以下几个特点：   dict 是用空间来换取时间的一种方法。
# 1. 查找和插入的速度极快，不会随着 key 的增加而增加；
# 2. 需要占用大量的内存，内存浪费多。
# 而 list 相反：
# 1. 查找和插入的时间随着元素的增加而增加；
# 2. 占用空间小，浪费内存很少。


A={'Mike':70,'John':25}
print(A['Mike'])   #删key用pop(key)   dict 的 key 必须是不可变对象。

# set 和 dict 类似，也是一组 key 的集合，但不存储 value。由于 key 不能
# 重复，所以，在 set 中，没有重复的 key。  ser([list])
p=set([1,2])
print(p)  #p.add()  p.remove()
# /set 可以看成数学意义上的无序和无重复元素的集合


# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量
p1=255
print(hex(p1))  #hex()函数 讲10进制转成16进制

# pass 可以定义一个什么也不做的函数pass  可以用来做占位符
def nop():
    pass
print(nop())

import math
# math 包可以使用sin cos等函数  坐标、位移和角度
def move(x,y,step,angle=0):
    nx=x+step*math.cos(angle)
    ny=y-step*math.sin(angle)
    return nx,ny
x,y=move(100,100,60,math.pi/6)
print(x,y)  #Python 的函数返回多值其实就是返回一个 tuple

a=float(input('请输入a:'))
b=float(input('请输入b:'))
c=float(input('请输入c:'))
# x1=((-b+math.sqrt(b**2-4*a*c))/(2*a))
# x2=((-b-math.sqrt(b**2-4*a*c))/(2*a))
# print('x1=',x1,'x2=',x2)

if a!=0:
    delta=b**2-4*a*c
    if delta<0:
        print('无根')
    elif delta==0:
        s=-b(2*a)
        print('唯一根x=',s)
    else:
        root=math.sqrt(delta)
        x1=(-b+root)/(2*a)
        x2=(-b-root)/(2*a)
print('x1=',x1,'x2=',x2)


# 先判断△=b²-4ac，若△＜0，则原方程无实根；

# 一元二次方程标准形式是ax²+bx+c=0，求根公式为x=[-b±根号下(b²-4ac)]/2a，
# 若△=0，则原方程有两个相同的解，为x=-b/2a，若△＞0，则x=(-b±根号下△)/2a；

# 配方法即先把常数c移到方程右边，再将二次项系数化为1，然后化简得-c/a=(b/2a)²，
# 若此式=0，则原方程有两个相同的解，为x=-b/2a；
# 若此式＞0，则x=[-b±根号下(b²-4ac)]/2a；
# 直接开平方法，形如（x-m）²=n(n＞0），可以直接得出x=m±根号n；

# 因式分解法，将标准方程化为（mx-n)(dx-e)=0的形式，直接求得x=n/m或x=e/d。

import random
random.seed(123)
for i in range(10):
    print(random.randint(1,999),end=',')
