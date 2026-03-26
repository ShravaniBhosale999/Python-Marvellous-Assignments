

class Demo:

    Value = 0
    def __init__(self, A, B):
        self.no1 = A
        self.no2 = B

    def fun(self):
        print("Inside fun method")
        print("No1 = ", self.no1)
        print("No2 = ", self.no2)

    def Gun(self):
        print("Inside Gun method")
        print("No1 = ", self.no1)
        print("No2 = ", self.no2)

# Creating objects
obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

# Calling methods
obj1.fun()
obj2.fun()
obj1.Gun()
obj2.Gun()