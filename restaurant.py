class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Restaurant Name: {self.name}")
        print(f"Food: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} is open")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors= ["vanilla", "chocolate", "mint", "strawberry", "mango"]

    def icecream_flavor(self):
        for flavor in self.flavors:
            print(flavor)


ice_cream_place = IceCreamStand("Aroma", "Cofee & Ice Cream")
ice_cream_place.icecream_flavor()