'''Inheritance and Advanced OOP Features
Create a base class Animal and a derived class Dog that inherits from Animal.
Output: 
Animals make different sounds.           # From Animal class
Dog barks!                               # From Dog Class'''

# Base class
class Animal:
   def sound(self):
      print("Animals make different sounds")

# Derived class
class Dog(Animal):
         def sound(self):
            super().sound()           # Calls the sound method from Animal
            print("Dog barks!")


# Create object of Dog and calls the method   
d = Dog()  
d.sound() 
