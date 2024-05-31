class Class:
    __number= 105
    def __privMeth(self):
        print("I'm inside class my Class")
    def hello(self):
        print("Private value:", self.__number)
private = Class()
private.hello()