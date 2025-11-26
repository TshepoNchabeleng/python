class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    def update_odometer(self, milleage):
        if milleage >= self.odometer:
            self.odometer = milleage
        else:
            print("You can't roll back the an odometer")
    def get_descriptive_name(self):
        longname = f"{self.year} {self.make} {self.model}\nmilleage: {self.odometer}km"
        return longname.title()
    

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kwh battery")
    

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name(), my_tesla.describe_battery())
        