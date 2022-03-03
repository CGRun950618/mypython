

# with open(r'D:\爬虫路径\a.txt','r',encoding='utf-8') as filtreader:
#     print(filtreader.readlines())
# encoding= utf-8

# 读取文件
# def read_file(pathfile):
#         with open(pathfile,'r') as fp:
#                 content=fp.read()
#                 return content
# ret=read_file('./a.txt')
# print(ret)
#
# def read_file(filepath):
#     fp=open(filepath)
#     content=fp.readlines()
#     fp.close()
#     return content
# ret=read_file('D:/爬虫路径/a.txt')
# print(ret)
# 当文件不在当前python文件同级目录时，可使用绝对路径,后者相对路径来确定文件的位置
#相对路径：指的是文件相对于(当前)工作目录所在的位置。

# 读写模式
def rw_file(filepath):
    with open(filepath,'r+',encoding='utf-8') as rwf:
        rwf.write('this is my wifis')
        content=rwf.read()
    return content
my_NewFile=rw_file('D:/爬虫路径/a.txt')
print(my_NewFile)

