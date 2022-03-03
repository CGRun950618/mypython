class Animal(object):
    def __init__(self,name):
        self.name=name
    def greet(self):
        print('Hello,I am %s.'%self.name)
dog1=Animal('xxx')
dog1.greet()

# print(dir(Animal))

class Dog(Animal):
    def greet(self):
        print ('xxw'+self.name)
dog=Dog('pig')
dog.greet()

class Cat(Animal):
    def greet(self):
        print('oop'+self.name)
cat=Cat('cat')
cat.greet()
# 继承可以拿到父类的所有数据和方法，子类可以重写父类的方法，也可以新增自己特有的方法
# 有了继承，才有多态，不同类的对象同一消息会做出不同的相应

# 类方法
class A(object):
    bar=1
    @classmethod
    def class_foo(cls):
        print('hello'),cls
        print(cls.bar)
A.class_foo()
# 装饰器classmethod可以通过类来调用方法

#静态方法： 在类中往往有一些方法跟类有关系，但是又不会改变类和实例状态 使用staticmethod 来装饰
class B(object):
    bar='FF'
    @staticmethod
    def static_foo():
        print ('hello'+B.bar)
B.static_foo()

# 1、普通函数（未定位在类里），都是函数。
# 2、静态方法（@staticmethod），都是函数。
# 3、类方法（@classmethod），都是方法。
# 4、实例方法（首参数为self且非静态、非类方法的），都是方法。

# 实例方法，第一个参数必须要默认传实例对象，一般习惯用self。
# 静态方法，参数没有要求。
# 类方法，第一个参数必须要默认传类，一般习惯用cls。


# 定制类和魔法方法
# __init__这些方法称为魔法方法和特色方法
# 创建一个类的实例时 类会先调用__new__(cls,[,...])来创建实例 然后__init__方法再对实例（self)进行初始化
# __new__时类方法，__init__时实例方法  重载__new__方法，需要返回类的实例
class C(object):
    _dict = dict()
    def __new__(cls):
        if 'key' in C._dict:
            print('exists')
            return  C._dict['key']
        else:
            print('new')
            return object.__new__(cls)
    def __init__(self):
        print('init')
        C._dict['key']=self
c1=C()
c2=C()


class Foo(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return 'Foo object (name：%s)'%self.name
    __repr__=__str__
print(Foo('ethan'))
print(Foo('ethan'.__str__()))
print(Foo('ethan'.__repr__()))
# 将某一类型的变量或者常量转换为字符串对象通常有两种方法，即str() 或者 repr()

# 这个数列从第3项开始，每一项都等于前两项之和。
# class Fib(object):
#     def __init__(self):
#         self.a,self.b=0,1
#     def __iter__(self):  #实例对象可被用于 for...in 循环，这时我们需要在类中定义 __iter__
#         return self
#     def __next__(self):  #next 返回容器的下一个元素，在没有后续元素时抛出 StopIteration 异常。
#         self.a,self.b=self.b,self.a+self.b
#         return self.a
# fib=Fib()
# for i in fib:
#     if i>100:
#         break
#     else:
#         print(i)

class Fib(object):
    def __getitem__(self, n):
        a,b=0,1
        for x in range(n):
            a,b=b,a+b
        return a
fib=Fib()
print(fib[5])


# nterms=int(input('你需要几项：'))
# n1=0
# n2=1
# count=2
# if nterms <=0:
#     print('请输入一个整数：')
# elif nterms==1:
#     print('斐波纳契数列')
#     print(n1)
# else:
#     print('斐波纳契数列')
#     print(n1,',',n2,end=',')
#     while count<nterms:
#         nth=n1+n2
#         print(nth,end=',')
#         n1=n2   # 更新值
#         n2=nth
#         count+=1



# __new__ 在 __init__ 之前被调用，用来创建实例。
# __str__ 是用 print 和 str 显示的结果，__repr__ 是直接显示的结果。
# __getitem__ 用类似 obj[key] 的方式对对象进行取值
# __getattr__ 用于获取不存在的属性
# obj.attr __call__ 使得可以对实例进行调用

class Point(object):
    def __init__(self,x,y):
        self.x,self.y=x,y
    def __call__(self,z):
        return self.x+self.y+z  #传入参数，对实例进行调用，对应p.__call__(6)
p=Point(3,4)
print(p(6))

class Pointt(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
p=Point(3,4)
p.z=6    #绑定一个新属性
print(p.z)
print(p.__dict__)  #字典格式

# 通过__slots__方法告诉python不要使用字典，而且只给一个固定集合的属性分配空间
class Pointtt(object):
    __slots__ = ('x','y','z')
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.z=None
    def tell_info(self,name):
        return getattr(self,name)   # __getattr__ 用于获取不存在的属性

o=Pointtt(8,9)
o.z=7
print(o.x)
print(o.tell_info('z'))
o.e=50  #设置一个不在__slots__中存在的属性，会报错
print(o._dict)
# slots 魔法：限定允许绑定的属性. __slots__ 设置的属性仅对当前类有效，对继承的子类不起效，除非子类也定义了 slots， 这样，子类允许定义的属性就是自身的 slots 加上父类的 slots。