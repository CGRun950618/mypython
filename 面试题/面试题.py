# encoding= utf-8

# 1.实现1到100之和
import random

print(sum(range(1,101)))

# 2.函数内部修改全局变量
a=5
def abc():
    global a
    a=1
abc()
print(a)

#3.删除键和合并2个字典
dic1={'name':'陈泡泡','age':'3'}
dic2={'name':'老蛇皮'}
del dic1['name']
# dic1.update(dic2) #字典构造器
# print(dic1)
d={**dic1,**dic2}   #3.5以上全新字典合并方式
print(d)

#4.列表去重
l=set([2,3,36,3,6,8,8])
for i in l:
    print(i)

#5.fun(*arg,**kwargs) 用于接收补丁参数
# *arg接收非键值对的可变参数得参数列表
# **kwargs允许接收不定长度得键值对


#6.列表[1,2,3.4,5]请使用map()函数输出[1,4,9,16,25],并输出大于>10得
b=[1,2,3,4,5]
def fun(x):
    return x**2
tmp=map(fun,b)     #map(function,iterable,...)提函数对指定序列做映射
res=[i for i in tmp if i>10]
print(res)


#7.生成随时整数,随机小数,0-1之前小数
b=random.randint(1,100)
print(b)
# import numpy  d=np.random.randn(5)
c=random.random()  #不用传参
print(c)

#8.<div class="nam">中国<div>用正则匹配
import re
p=r'<div class ="name">中国</div>'
pl=r'<div class=".*">(.*?)<div>'
patternl=re.compile(pl)
reb=patternl.findall(p)
# reb=re.findall(r'<div class=".*">(.*?)<div>',p)
print(reb)

#用lambda函数实现两个函数相乘
Fn=lambda x,y:x*y
print(Fn(2,3))