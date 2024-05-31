class Cir:
    def __init__(self, r):
        self.radi = r
    def area(self):
        return 3.141 * self.radi ** 2
    def perimeter(self):
        return 2 * 3.141 * self.radi
Obj = Cir(9)
print("Area:", Obj.area())
print("Perimeter:", Obj.perimeter())
