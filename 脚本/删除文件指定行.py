# def Del_line(file_path,line_num):
#     with open(file_path,"r") as f:
#         res=f.readlines()  #res为列表
#     res.pop(int(line_num)-1)
#
#     with open(file_path,"w") as f:
#         f.write("".join(res))  #将res转换成字符串重写写入到文本
# Del_line("", 518)

fin =open('汕尾地市4G基站补录数据20220111', 'r')
a=fin.readlines()
fout=open('汕尾地市4G基站补录数据20220111', 'w')
b=''.join(a[:5705])
fout.write(b)   #只读518行后面得所有，从0算起

# def Del_line(file_path,line_num):
#     file = open(file_path,"r")
#     for num,value in enumerate(file,1):
#         if num == line_num:
#             with open(file_path,'r') as r:
#                  lines=r.readlines()
#             with open(file_path,'w') as w:
#                 for nr in lines:
#                     if value not in nr:
#                         w.write(nr)
#     file.close()
#     return
# Del_line("test.txt",18398)