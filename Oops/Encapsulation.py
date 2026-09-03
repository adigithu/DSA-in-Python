class Car:
    def __init__(self, userbrand, usermodel):
        self.__brand=userbrand
        self.model=usermodel

    def get_brand(self):
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size
my_car=ElectricCar("Tesla", "Model S", "100kWh")
print(my_car.get_brand())