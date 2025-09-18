# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 13:51:45 2025

@author: JENIL
"""

class Car:
    # Constructor to initialize the object
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    # Method to describe the car
    def car_details(self):
        return f"Car: {self.brand}, Model: {self.model}"

# Creating an object of the Car class
my_car = Car("Toyota", "Fortunar")
print(my_car.car_details())  
