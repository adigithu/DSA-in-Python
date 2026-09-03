class Car:
    def __init__(self, userbrand, usermodel):
        self.brand=userbrand
        self.model=usermodel

    def full_name(self):
        return f"{self.brand} {self.model}"
a=Car("Toyota", "Corolla")
print(a.full_name())