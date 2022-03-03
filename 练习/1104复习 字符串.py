floewr=[0,1,2,3,4,5,6]
print(floewr[:])  #全复制
print(floewr[0:1]) #输出第一个值
print(floewr[0:2])  #输出0，1
print(floewr[:2])   #输出0，1
print(floewr[0:6:2])  #输出0，2，4
print(floewr[0:6:-1])   #输出空，负补长时左索引要大于右索引
print(floewr[-3])  #输出4
print(floewr[-3:])  #输出最后面3个

#x.index() 用于找出某个元素的位置，如果有相同的元素，则返回第一个元素的位置
#x.append ()方法用于在列表末尾增加新元素
#x.count（）用于统计元素出现次数
#x.extend（） 把B的第二位值插入A中 append方法是将其作为一个元素添加到列表中，而extend则是将新列表的元素逐个添加到原列表中。
B=[0,2,1]
floewr.extend(B[1:3])
print(floewr)
#x.reverse()  将元列表素反转
#x.renmove #将括号里面的值删除匹配到第一个值，括号里面不能为空
#x.sort #对列表进行排序，注意该方法改变原来的列表，而不是返回新的排序列表，另外sort方法的返回值是空。
B.sort(reverse=True)  #反向排序

print(B)
C=sorted(B)  #原列表没有改变
print(C)  #sort和sorted函数默认排序都是升序

students={
    ('john','a',15),
    ('mark', 'x', 75),
    ('xixi', 'o', 85),
    ('kok', 'u', 33),
}
b=sorted(students,key=lambda student:student[2])
c=sorted(students,key=lambda student:(student[1],-student[2]))
print(b)
print(c)

d=(12,) #元组后面要有扩号

#字符串
f='hello,' #字符也是一种序列，通用的序列的操作，比如索引，分片，加法，乘法
print(f[0]) #索引
print(f[1:3])  #分片
print(f+'world')  #加法
print(f*2) #乘法
# f[1]='ab'   字符和元组一样是不可变的 不能赋值
# print(f)
print(f.find('e'))  #find反方法用于在一个字符串查找子串
print('/user/bin/ssh'.split('/'))   #split使用'/'做分割  不提供分割符默认所有的空格作为分割符（空格，制表符，换行）
# print('+'.join(['0','1','2']))   #join 逆用split
# print(' hello%'.strip('% ')) #strip 移除指定的符合 左右两边 移除指定的空格
# g='To be no.1'
# print(g.replace('To','to'))  #to替换To返回一个新的字符串 原字符串不变replace
#
# # str.translate(table[,deletechars]); translate 和replace方法类似
# # table -- 翻译表，翻译表是通过maketrans方法转换而来。
# # deletechars -- 字符串中要过滤的字符列表
#
# # 注：Python3.4已经没有string.maketrans()了，取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans()
# # tr.maketrans(intab,outtab[,delchars])  python3
# # import string string.maketrans(intab,outtab)  python2
# #intab与outtab的长度务必相等。
# intab='abcdedf'
# outtab='1234567'
# deltab='cde'
# trantab1=str.maketrans(intab,outtab)  #创建字符映射转换表
# trantab2=str.maketrans(intab,outtab)   #创建字符映射转换表，并删除字符
# test='this  is one sb'
# print(test.maketrans(trantab1))

table=str.maketrans('cdef','1234')
bus='this is one fuckpig'
print(bus.translate(table))

X='PYTHON'
print(X.lower())  #lower转小写  upper转大写


