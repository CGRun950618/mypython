# -*- coding:utf-8 -*-

import sys
import hashlib
import time

#返回当前计算机时间
start = time.perf_counter()

result = open("result.txt",'w')

#打开密码本
f = open("dic.txt",'r',encoding='utf-8')
#读取密码数据本
data = f.read().splitlines()
#循环密码数据
for i in data:
    # k = open(sys.argv[1],'r',encoding='utf-8')
    #打开用户名本
    k = open("username.txt",'r',encoding='utf-8')
    data1 = k.read().splitlines()
    #循环用户名
    for j in data1:
        #拼接密码和用户名
        res = i + "" + j
        #生成实例
        b = hashlib.sha1()
        b.update(res.encode(encoding='utf-8'))


        h = open("woqimini.txt",'r',encoding='utf-8')
        data2 = h.read().splitlines()

        for l in data2:
                if b.hexdigest()==l:
                    print('yes')
                    result.write("[username]: "+j+'\n')
                    result.write("[password]: "+i+'\n')
                    result.write("[salt-passwd]: "+b.hexdigest()+'\n\n\n')
result.close()


end = time.perf_counter()
print (end - start)
