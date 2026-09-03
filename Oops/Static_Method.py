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

    @staticmethod
    def description():
        return "Cars"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric Charge"
    
print(Car.description())
