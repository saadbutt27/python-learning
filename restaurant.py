class Restaurant:
    """Making a restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name: {self.restaurant_name.title()}\nCuisine Type: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is open!")

    def set_number_served(self, start):
        if (start >= 0):
            self.number_served = start

    def increment_number_served(self, increment):
        if (self.number_served + increment >= 0):
            self.number_served += increment
