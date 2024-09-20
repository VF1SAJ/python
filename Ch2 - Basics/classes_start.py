#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
# class is to hold information
# __init__ constructed and initialized
# Class: A blueprint for creating objects. It encapsulates data for the object and methods to manipulate that data. For example, in the video, a Vehicle class is created to represent vehicles with properties like body_style and methods like drive.
# Function (def): A block of reusable code that performs a specific task. Functions can be defined inside or outside of classes. In the video, the __init__ method and drive method are functions defined within the Vehicle class to initialize and manipulate vehicle objects.
# To summarize:
# Class: Defines a type of object and its behavior.
# Function: Defines a specific action or behavior, which can be used within or outside of a class.

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle
    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

#Define the Car class derived from Vehicle
class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)

#Define the Motorcycle class derived from Vehicle
class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if (hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed)

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)

car1.drive(30)
car2.drive(40)
mc1.drive(50)


