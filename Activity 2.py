class Computer:
    def __init__(self):
        self.__maxprice=1000

    def sell(self):
        return "The selling price is",self.__maxprice
    
    def setmaxprice(self,price):
        self.__maxprice=price
        return "Max price is ",self.__maxprice
    
c=Computer()
print(c.sell())

c.__maxprice=1100
print(c.sell())

c.setmaxprice(1100)
print(c.sell())