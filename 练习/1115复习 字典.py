
do={}  #空字典
print(do)

d1={'name':'ethan','age':21}
print(d1)
d1['age']=23   #更新字典
print(d1)

d2=dict(name='ehtan',age=20)  #dict函数是创建一个字典
print(d2)

item=[('name','ehan'),('age',20)]
print(dict(item))

for key in list(d1.keys()):
    if key=='age':
        del d1[key]
print(d1)

# rv=d1.clear()  #清空
# print(rv)  #输出none 无返回值

# copy 方法实现的是浅复制（shallow copy）。它具有以下特点： 对可变对象的修改保持同步； 对不可变对象的修改保持独立；
# name 的值是不可变对象，books 的值是可变对象
d3={'name':'make','books':['book','book2','book3']}
d4=d3.copy()
d4['name']='peter'  #对不可变的对象的修改不会改变d3
print(d4)
d4['books'].remove('book2')
print(d3)   #会把d3的也清掉， d3的可变对象也会影响d4
print(d4)

#不可变对象：字符int long float，数字，元组，布尔bool
#可变对象：列表，字典
#deep copy 深复制：它会创造出一个副本，跟原来的对象没有关系，可以通过 copy 模块的 deepcopy 函数来实现：
from copy import deepcopy
d5={'name':'make','books':['book','book2','book3']}
d6=deepcopy(d5)  #创造出一个副本
d6['books'].remove('book2')
print(d5)   #不会改d5

# print(do['name'])  输出KeyError报错 使用get可以避免
print(do.get('name'))

d7={'age':20,'name':'lebron'}
d7.setdefault('age',18)  #如果存在则返回存在的值，不存在则更新字典值
print(d7)

d8={'name':'joke'}
do.update(d8)  #将字典d8添加到do
print(do)

#items方法将所有字典以列表形式返回 iteritems返回迭代器对象而不是列表
print(d7.items())
for k,v in d7.items():
   '%s: %s' % (k,v)
print(d7)

#将字典的键和值分别以列表形式返回 iterkeys--针对键的迭代器对象 itervaluses 针值的迭代器对象
print(d7.keys(),d7.values())

# d7.pop('name')
# print(d7)
print(d7.popitem()) #随机移除字典中某个键值对

#sorted
students=[
    {'name':'john','score':'B','age':15},
    {'name': 'kobe', 'score': 'A', 'age': 25},
    {'name': 'lebron', 'score': 'C', 'age': 14}
]
print(sorted(students,key=lambda stu:stu['score'])) #分数从小到大
print(sorted(students,key=lambda stu:stu['score'],reverse=True))
print(sorted(students,key=lambda stu:(stu['score'],stu['age']))) #分数从小到大，再从年龄从小到大，数字相反在前面加个-








