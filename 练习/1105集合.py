# 集合（set）和字典（dict）类似，它是一组 key 的集合，但不存储 value。集合的特性就是： key 不能重复]
s1=set('helloworld')  #接收一个字符串，然后遍历它
print(s1)
for e in s1:
    print (e) #遍历集合
s1.add('s')   #加一个元素
print(s1)
s1.remove('d')   #删除一个元素，如果元素不存在则用discard()
print(s1)

s2={1,2,3,4}
s3={3,4,5,6}
print(s2&s3)  #交集
print(s2|s3)   #并集
print(s2-s3)  #差集
print(s3.issubset(s2))  #s3是否是s2的子集  false
print(s3.issuperset(s2))  #s3是否是s2的超集 false