'''Introduction to OOP Concepts
Create a class Person with attributes name and age. Create an object and display its details.
Input: Person("Alice", 25)
Output: Name: Alice, Age: 25'''


class Person:                                             # Created a class named Person
    def __init__(self, name, age):                        # Constructor method to initialize name and age
        self.name = name
        self.age = age

    def __str__(self):                                   # Special method that defines what to show when the object is printed
        return f"Name: {self.name}, Age: {self.age}"     # Returns readable string representation

p1 = Person("Alice", 25)                                 # Creates an Person object with name and age value
print(p1)                                                # Calls __str__() automatically and prints Name: Alice, Age: 25
