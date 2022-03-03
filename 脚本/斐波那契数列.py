# def Fibonacci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return Fibonacci(n-1)+Fibonacci(n-2)
# my_math=Fibonacci(6)
# print(my_math)
#
# # f(1)=0
# # f(2)=1
# # f(3)=f(2)+f(1)=0+1=1
# # f(4)=f(3)+f(2)=1+1=2
# # f(5)=f(4)+f(3)=2+1=3
# # f(6)=f(5)+f(4)=3+2=5
#
# # 递归自顶向下的方式效率太低，我们采用自底向上的方式，先将数值正向放入列表中，最后从列表中取值。
# def Fibonaccii(n):
#     seq=[0,1]
#     if n==1:
#         return [0]
#     elif n==2:
#         return[0,1]
#     else:
#         for i in range(n-2):
#             seq.append(seq[i]+seq[i+1])
#         return seq[-1]
# my_maths=Fibonaccii(6)
# print(my_maths)
#
# def Fibonacciii(n):
#     seq=[0,1]   #初始化列表
#     i=0    #初始i
#     if n==0:  #如果n=0，返回列表[0]
#         return [0]
#     else:
#         if n<=3:  #如果0<n<3
#             for i in range(n):
#                 seq.append(seq[i]+seq[i+1])
#             return seq
#         else:
#             while True:   #理论上当n不确定时，需要添加的项数也是不确定的，故死循环
#                 if seq[-1]<=n:   #一直添加，如果添加的最后一项不大于给定值
#                     seq.append(seq[i]+seq[i+1])
#                     i+=-1   #每次循环i 递增
#                     continue   #继续循环，不执行以下代码
#                 break #当最后一项大于给定值时，跳出死循环
#             return seq[0:-1]   #放回最后一个数值
# my_mathss = Fibonacciii(3)
# print(my_mathss)

def Fibonacciiii(n):
    seq=[0,1]
    if n==1:
        return [0]
    elif n==2:
        return [0,1]
    else:
        for i in range(n-2):
            seq.append(seq[i]+seq[i+1])
        return seq
my_mathsss = Fibonacciiii(18)
print(my_mathsss)
