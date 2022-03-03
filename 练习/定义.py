def greet_user(username):
    """简单的问候语"""
    print("hello!"+username+"!")
greet_user('jess')
#
# def greet_city(city):
#      """"城市"""
#      print("hello"+city+"!")
# greet_city(input(""))

# def active(suject):
#     print("你想上什么课呢"+suject)
# active(input())

def pet(zoo_name,zoo_weight):
    print('这是一只'+zoo_name)
    print('大概有'+zoo_weight+'斤')
pet('pig','50')
pet('dog','40')


# def get_formatted_name(first_name,last_name):
#     """"返回整洁的姓名"""
#     full_name=first_name+""+last_name
#     return full_name.title()
# while True:
#     print("\n please tell me your name:")
#     print("(enter 'q' at any time to quit)")
#     f_name=input("(First name:)")
#     l_name=input("(last name:)")
#     if f_name=='q':
#         break
#     if l_name=='q':
#         break
#     formatter_name=get_formatted_name(f_name,l_name)
#     print("\n hello,"+formatter_name+"!")

# def greet_user(names):
#     """跟列表中的每位用户"""
#     for name in names:
#         msg="hello,"+name.title()+"!"
#         print(msg)
# username=['peter','julie','mark']
# greet_user(username)

# def profession(sorts):
#     """职业分类"""
#     for sort in sorts:
#         work="他是一名"+sort
#         print(work)
# working=['警察','医生','教师']
# profession(working)

def police(sorts):
    for sort in sorts:
        work ='他是一名'+ sort
        print(work)
working=['医生','警察','护士']
police(working)


