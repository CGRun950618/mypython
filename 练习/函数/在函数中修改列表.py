# unprinted_designs=['ipone case','robot pendant','dodeccahedron']
# completed_midels=[]
# while unprinted_designs:
#     current_desgin=unprinted_designs.pop()
#     print("Print model:"+current_desgin)
#     completed_midels.append(current_desgin)
# print("\n The following models have been printed:")
# for completed_midel in completed_midels:
#     print(completed_midel)

def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile
user_profile=build_profile('albert','einstein',location='princeton',field='physics')
print(user_profile)

ip=build_profile('mark','jordan',basketball='NBA',contray='USA')
print(ip)


