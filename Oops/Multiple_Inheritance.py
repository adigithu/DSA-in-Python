class Car:
    def __init__(self, userbrand, usermodel):
        self.__brand=userbrand
        self.model=usermodel

    def get_brand(self):
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric Charge"

class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def Engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_tesla=ElectricCarTwo("Tesla", "Model 5")
print(my_tesla.battery_info())
print(my_tesla.Engine_info())