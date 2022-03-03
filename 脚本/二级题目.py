# #1.获得用户输入的整数N，计算并输出N的32次方
# N=eval(input('请输入：'))#eval函数实现list，dict,tuple,int与str直接的转化
# a=N**32
# print("它的次方"+str(a))
#
# # 2.获得用户输入的一段文字，将这段文字进行垂直输出
# s=input('用户输入字段：')
# # for i in s:
# #     print(i+'\t')
# i=0
# while i<len(s):
#     print(s[i])
#     i=i+1
#
# #获得用户输入的一个合法算式
# a=input('请输入一个带数算式：')
# b=eval(a)
# print('结果为：'+str(b))

#获得用户输入的一个小数，提取并输出整数部分
# # b=eval(input('请输入一个小数：'))
# # print('%d'%b)
# b=input('请输入一个小数：')
# l=len(b)
# i=0
# while i<1:
#     print(b[i],end='')
#     i=i+1
#     if b[i]=='.':
#         break

#获得用户输入的一个整数，输出该整数百位以上的数字
# a=input('请输入一个整数：')
# b=eval(a)
# if type(b)==type(12345):       #type(object)可以直接返回变量类型 #type()返回 int  当只有一个对象，返回对象的类型   当有三个参数时返回一个类对象
#     c=a[:-2]                    #isinstance()函数判断变量的类型  返回布尔值True False
#     print(c)
# else:
#     print("请输入一个整数")
#
# a=1253
# c=[int(item) for item in str(a)]  #int 转列表
# print(c[:-2])

#获得用户输入的字符从串，将字符串按照空格分隔，逐行打印
s=input('请输入字符串：')
a=s.split(' ',3)    #以空格为分隔符，分隔成两个  str.split(' ', 1 )以空格为分隔符，分隔成两个
l=len(a)      #os.path.split()：按照路径将文件名和路径分割开
for i in range(l):
    print(a[i])

