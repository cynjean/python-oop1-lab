#!/usr/bin/env python3
# Create coffee class
class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    # Create getters and setters
    def get_size(self):
        return self._size

    def set_size(self, size):
        if size in ["Small", "Medium", "Large"]:
            self._size = size
        else:
            print("size must be Small, Medium, or Large")

    size = property(get_size, set_size)
    

    # Create tip method 
    def tip(self):
        self.price += 1
        print ("This coffee is great, here’s a tip!")

# Create coffee instances
black = Coffee(size = "Large", price = 1.50)
latte = Coffee(size = "Large", price = 2.50)
americano = Coffee(size = "Large", price = 3.50)



