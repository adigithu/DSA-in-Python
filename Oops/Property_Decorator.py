class Car:
    def __init__(self, brand, model):
        self.__brand=brand
        self.__model=model

    def get_brand(self):
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod
    def description():
        return "Cars"

    @property
    def model(self):
        return self.__model

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

    def fuel_type(self):
        return "Electric Charge"
    
my_car=Car("Tata", "Safari")
Car("Tata", "Nexon")
print(my_car.model)
