# class Exam(object):
#     def __init__(self,score):
#         self._score=score
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self,val):
#         if val<0:
#             self._score=0
#         elif val>100:
#             self._score=100
#         else:
#             self._score=val
# e=Exam(101)
# print(e.get_score())
# e.set_score(70)
# print(e.get_score())

class Exam(object):
    def __init__(self,score):
        self._score=score
    @property   #加上@property我们可以把score当成一个属性来用
    def score(self):
        return self._score
    @score.setter  #他可以把装饰的方法变成属性来赋值   没有这个只能是只读
    def score(self,val):
        if val<0:
            self._score=0
        elif val>100:
            self._score=100
        else:
            self._score=val
e=Exam(60)
print(e.score)
e.score=90
print(e.score)
e.score=200
print(e.score)


# 重定义某个方法，该方法会覆盖父类的同名方法，但有时，我们希望能同时实现父类的功能，这时，我们就需要调用父类的方法了，可通过使用 super 来实现
class Animal(object):
    def __init__(self,name):
        self.name=name
    def greet(self):
        print('hello,I am %s.'% self.name)

class Dog(Animal):
    def greet(self):
        super(Dog,self).greet()
        print('wwwww')

dog=Dog('dog')
dog.greet()

# class Base(object):
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
# class A(Base):
#     def __init__(self):
#         super(A, self).__init__(a,b)
#         self.c=c
# 实际上是实例化了一个 super 类。你没看错， super 是个类，既不是关键字也不是函数等其他数据结构:
# 提供一个 MRO 以及一个 MRO 中的类 C ， super() 将返回一个从 MRO 中 C 之后的类中查找方法的对象。


class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        # 第四步
        # 来自 D.add 中的 super
        # self == d, self.n == d.n == 5
        print('self is {0} @A.add'.format(self))
        self.n += m
        # d.n == 7


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        # 第二步
        # 来自 D.add 中的 super
        # self == d, self.n == d.n == 5
        print('self is {0} @B.add'.format(self))
        # 等价于 suepr(B, self).add(m)
        # self 的 MRO 是 [D, B, C, A, object]
        # 从 B 之后的 [C, A, object] 中查找 add 方法
        super().add(m)

        # 第六步
        # d.n = 11
        self.n += 3
        # d.n = 14

class C(A):
    def __init__(self):
        self.n = 4

    def add(self, m):
        # 第三步
        # 来自 B.add 中的 super
        # self == d, self.n == d.n == 5
        print('self is {0} @C.add'.format(self))
        # 等价于 suepr(C, self).add(m)
        # self 的 MRO 是 [D, B, C, A, object]
        # 从 C 之后的 [A, object] 中查找 add 方法
        super().add(m)

        # 第五步
        # d.n = 7
        self.n += 4
        # d.n = 11


class D(B, C):
    def __init__(self):
        self.n = 5

    def add(self, m):
        # 第一步
        print('self is {0} @D.add'.format(self))
        # 等价于 super(D, self).add(m)
        # self 的 MRO 是 [D, B, C, A, object]
        # 从 D 之后的 [B, C, A, object] 中查找 add 方法
        super().add(m)

        # 第七步
        # d.n = 14
        self.n += 5
        # self.n = 19

d = D()
d.add(2)
print(d.n)

# [__main__.C, __main__.A, __main__.B, __main__.Base, object]
# 一个类的 MRO 列表就是合并所有父类的 MRO 列表，并遵循以下三条原则：
# 子类永远在父类前面
# 如果有多个父类，会根据它们在列表中的顺序被检查
# 如果对下一个类存在两个合法的选择，选择第一个父类


# class B(A1,A2,A3 ...)
# 这时B的mro序列 mro(B) = [B] + merge(mro(A1), mro(A2), mro(A3) ..., [A1,A2,A3])
# merge操作就是C3算法的核心。


# class A(O):pass
# class B(O):pass
# class C(O):pass
# class E(A,B):pass
# class F(B,C):pass
# class G(E,F):pass


# A、B、C都继承至一个基类，所以mro序列依次为[A,O]、[B,O]、[C,O]
# mro(E) = [E] + merge(mro(A), mro(B), [A,B])
#        = [E] + merge([A,O], [B,O], [A,B])
# 执行merge操作的序列为[A,O]、[B,O]、[A,B]
# A是序列[A,O]中的第一个元素，在序列[B,O]中不出现，在序列[A,B]中也是第一个元素，所以从执行merge操作的序列([A,O]、[B,O]、[A,B])中删除A，合并到当前mro，[E]中。
# mro(E) = [E,A] + merge([O], [B,O], [B])
# 再执行merge操作，O是序列[O]中的第一个元素，但O在序列[B,O]中出现并且不是其中第一个元素。继续查看[B,O]的第一个元素B，B满足条件，所以从执行merge操作的序列中删除B，合并到[E, A]中。
# mro(E) = [E,A,B] + merge([O], [O])
#        = [E,A,B,O]


