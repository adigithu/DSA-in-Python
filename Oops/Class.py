class Car:
    def __init__(self, userbrand, usermodel):
        self.brand=userbrand
        self.model=usermodel
a=Car("Toyota", "Corolla")
print(a.brand)