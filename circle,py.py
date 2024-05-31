class Cir:
    def __init__(self, numbers):
        self.num = numbers
    def read_num(self):
        print(self.num)
num_list = [10, 501, 22, 37, 100, 999, 87, 351]
obj = Cir(num_list)
obj.read_num()