# class refrigerator():
#     """初始化冰箱属性"""
#     def __init__(self,size,brand):
#         self.size=size
#         self.brand=brand
#     def get_refrigerator(self):
#         refrigerator=self.size+self.brand
#         return  refrigerator.title()
# my_new_refrigerator=refrigerator('new','55')
# print(my_new_refrigerator.get_refrigerator())


class drinks():
    """初始化饮料属性"""
    def __init__(self,milk,coffee,wine):
        self.milk=milk
        self.coffee=coffee
        self.wine=wine
    def get_drinks(self):
        drinks=self.milk+""+self.coffee+""+self.wine
        return drinks.title()
my_new_drinks=drinks('蒙牛','蓝山','青岛')
print(my_new_drinks.get_drinks())