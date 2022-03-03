# ip=input('请输入你的ip地址：')
# print(ip)

crrunt_number=1
while crrunt_number<=5:
    print(crrunt_number)
    crrunt_number+=1

# mark="\nplease enter the city:"
# mark_1="enter 'quit'  when you finished"
# while True:
#     city=input(mark)
#     if city=='quit':
#         break
#     else:
#         print(mark+city+'!')

ip="'请输入你的IP地址':"
# ip_1="enter 'quit' "
while True:
    address=input(ip)
    if address=='quit':
        break
    else:
        print("你的本地IP是"+address)


