# encoding= utf-8
import  time
import  hashlib

text1='EWkq4AnnV@'
sha=hashlib.sha1()#生成实例

sha.update(text1.encode('utf-8'))  #将上面字符串传入
text1_sha=sha.hexdigest()  #返回摘要，作为十六进制数据字符串值
print(text1_sha)

text2='python hashlib?'
md5=hashlib.md5()
md5.update((text2.encode('utf-8')))
text2_md5=md5.hexdigest()
print(text2_md5)

# start=time.perf_counter()
# time.sleep(10)
# end=time.perf_counter()
# dur=start-end
# print(dur)
