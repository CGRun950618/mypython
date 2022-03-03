# class Car():
#     """一次模拟汽车的简单尝试"""
#     def __init__(self,mark,model,year):
#         """初始化描述汽车的·属性"""
#         self.mark=mark
#         self.model=model
#         self.year=year
#         self.mileage=0
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#         long_name=str(self.year)+' '+self.mark+' '+self.model
#         return  long_name.title()
#     def get_mileage(self):
#         print("这辆车行驶了"+str(self.mileage)+"公里")
# my_new_car=Car('audi','a4',2016)
# print((my_new_car.get_descriptive_name()))
# my_new_car.get_mileage()
# my_new_car.mileage=23
# my_new_car.get_mileage()
#


# # 函数的一切都适用于方
# # 方法的self 是指向的自动传参
#
# class clothes():
#     """买衣服"""
#     def __init__(self,brand,color,size):
#         """初始化衣服属性"""
#         self.brand=brand
#         self.color=color
#         self.size=size
#     def get_clothes_message(self):
#         message=self.brand+" "+self.color+" "+self.size
#         return message.title()
# my_new_clothes=clothes('fila','42','yellow')
# print(my_new_clothes.get_clothes_message())
#
# class door():
#     """铁门的属性"""
#     def __init__(self,size,nature):
#         self.size=size
#         self.nature=nature
#     def get_door(self):
#         door=self.size+""+self.nature
#         return  door.title()
# my_new_door=door('525','wood')
# print(my_new_door.get_door())

#
# class Car():
#     def __init__(self,brand,year,t_car):
#         self.brand=brand
#         self.year=year
#         self.t_car=t_car
#     def get_car(self):
#         message=self.brand+""+self.year+''+self.t_car
#         return message.title()
#     def p_car(self):
#         print('这辆车行驶了'+self.t_car)
# my_new_car=Car('toyot','5','52')
# print(my_new_car.get_car())
# my_new_car.t_car='23'
# my_new_car.p_car()

# 设置了值不能回调
# class Car():
#     def __init__(self,brand,year):
#         self.brand=brand
#         self.year=year
#     def get_car(self):
#         message=self.brand+""+self.year+''
#         return message.title()
#     def t_car(self,mileage):
#         self.mileage='34'
#         if mileage>=self.mileage:
#             self.mileage=mileage
#         else:
#             print("your can't rock")
#     def p_car(self):
#         print('这辆车行驶了'+self.mileage+'ms')
# my_new_car=Car('benz','256')
# print(my_new_car.get_car())
# my_new_car.t_car(input())
# my_new_car.p_car()

class Car():
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def get_car(self):
        message=self.brand+""+self.year+''
        return message.title()
    def t_car(self,mileage):
        self.mileage='34'
        if mileage>=self.mileage:
            self.mileage=mileage
        else:
            print("your can't rock")
    def p_car(self):
        print('这辆车行驶了'+self.mileage+'ms')
    def intcrement_car(self,mileage):
        self.mileage+=mileage
# my_new_car=Car('benz','256')
# print(my_new_car.get_car())
# my_new_car.t_car(input())
# my_new_car.p_car()
# my_new_car.intcrement_car('5')
# my_new_car.p_car()

class electricCar(Car):
    def __init__(self,brand,year):
        super().__init__
my_tsela=electricCar('teasl',15)
print(my_tsela.get_car())
