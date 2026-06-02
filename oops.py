# classes and oops in python 
# object oriented programming is a programming paradigm that uses objects and classes to design and implement programs.
# class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.
# syntax: class ClassName:
#     # class body  
#     def method_name(self, parameters):
#         # method body


# object is an instance of a class. It is created from a class and has the attributes and methods defined in the class.
# syntax: object_name = ClassName()

from abc import abstractmethod


class Person:
    # constructor method
    # it is called when an object is created from the class. It initializes the attributes of the object.
    # syntax: def __init__(self, parameters):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
# creating an object from the class
# person1 = Person("juned", 25)
# print(person1.greet())

# inheritance is a mechanism in which a new class (called child class) is derived from an existing class (called parent class). 
# The child class inherits the attributes and methods of the parent class and can also have its own attributes and methods.
# syntax: class ChildClass(ParentClass):

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str):
        # super() is a built-in function that returns a temporary object of the superclass that allows you to call its methods.
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying. Student ID: {self.student_id}"

# encapsulation is a mechanism in which the data (attributes) and the code (methods) that manipulates the data are bundled together.
# It restricts direct access to some of the object's components, which can prevent the accidental modification of data.
# syntax: class ClassName: 
#     def __init__(self):
#         self.__private_attribute = value
#     def public_method(self):
#         # code that can access the private attribute 
class BankAccount:
    def __init__(self, account_number: str, balance: float):
        self.account_number = account_number
        self.__balance = balance  # private attribute

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            return f"Deposited {amount}. New balance: {self.__balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount: float):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew {amount}. New balance: {self.__balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def get_balance(self):
        return f"Current balance: {self.__balance}"

# bank_account = BankAccount("123456789", 1000.0)
# print(bank_account.account_number)  # This will work because account_number is a public attribute
# print(bank_account.__balance)  # This will raise an AttributeError because __balance is a private attribute

# polymorphism is a mechanism in which a single function or method can work in different ways based on the input or the context.
# syntax: def function_name(parameters):

class Shape:
    def area(self):
        pass    

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    

# abstract class is a class that cannot be instantiated and is meant to be subclassed. 
# It can contain abstract methods, which are methods that are declared but not implemented in the 
# abstract class. The subclasses of the abstract class must implement the abstract methods.
# syntax: from abc import ABC, abstractmethod
# class AbstractClass(ABC):
#     @abstractmethod
#     def abstract_method(self):
#         pass 

# example of abstract class and method
class Animal:
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
class Bird(Animal):
    def make_sound(self):
        return "Chirp!"
    

cat = Cat()
print(cat.make_sound())  # Output: Meow!
