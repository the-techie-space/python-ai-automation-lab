
# class : A class is a blueprint or template that defines properties (variables) and behaviors (methods).
# An object is an instance of a class.

# What is self?
# Refers to the current object
# Used to access instance variables and methods
# Without self, instance variables won’t work

class Car:
    def drive(self):
        print("Car is driving")

c1 = Car()   # object
c1.drive()

#Class = blueprint, Object = real-world instance

# __init__ Method (Constructor)

# Automatically called when an object is created

# Used to initialize object data

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Alice", 30)
print(p1.name, p1.age)

# __init__ is Used for initializing instance variables


# Instance Variables vs Class Variables
# 🔹 Instance Variables

# Belong to each object

# Defined using self

# 🔹 Class Variables

# Shared across all objects

# Defined inside class but outside methods

class Employee:
    company = "Dell"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable

e1 = Employee("John")
e2 = Employee("Emma")

print(e1.name, e2.company)


# Inheritance
# One class (child) inherits properties and methods of another class (parent).

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()
d.bark()

# polymerphism
# Same method name, different behavior.
# (Method overriding) basically the child class method will be called and print statements init
class Bird:
    def sound(self):
        print("Bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp")

b = Sparrow()
b.sound()

# Achieved via method overriding in Python


# Encapsulation (basically Restricting direct access to variables) ## Protects sensitive data

# Bundling data and methods together

# Restricting direct access to variables

# 🔹 Access Modifiers in Python

# Public → var

# Protected → _var

# Private → __var


class Account:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = Account()  # object creation → __init__ is called
acc.deposit(500)  # calling public method
print(acc.get_balance()) # prints balance


# __balance is private

# You cannot access it directly

# You must use methods (deposit, show_balance)

# What happens if you try to access it directly?

# print(acc.__balance)

# AttributeError: 'Account' object has no attribute '__balance'

# one line say for encapsulation is : 👉 Private variables are accessed indirectly using public methods, not directly.


# Quick Interview Summary (One-liners)

# Class: Blueprint

# Object: Instance of class

# __init__: Constructor

# Instance variable: Object-specific

# Class variable: Shared

# Inheritance: Code reuse

# Polymorphism: Same method, different behavior

# Encapsulation: Data hiding

# Abstraction: Hide implementation

# self: Refers to current object

# Overriding: Redefine parent method


# 1. Abstract Class vs Abstract Method

from abc import ABC, abstractmethod

# Abstract Class - Cannot instantiate, can have concrete methods
class BasePage(ABC):
    
    def __init__(self, driver):
        self.driver = driver
    
    # Concrete method (implemented)
    def click_element(self, locator):
        self.driver.find_element(*locator).click()
    
    # Abstract method (must be implemented by child)
    @abstractmethod
    def verify_page_loaded(self):
        pass

# Cannot do: base = BasePage(driver)  # TypeError!

# Child class MUST implement abstract methods
class LoginPage(BasePage):
    def verify_page_loaded(self):
        assert "Login" in self.driver.title


# Key Points:

# Abstract Class: Template with some implemented methods
# Abstract Method: Method signature only, child MUST implement


# 2. Abstract Class vs Interface (Python doesn't have interfaces, uses ABC)

from abc import ABC, abstractmethod

# Python's ABC is like Interface when ALL methods are abstract
class IDatabase(ABC):
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass
    
    @abstractmethod
    def close(self):
        pass

# Abstract Class - Mix of abstract and concrete
class BaseTest(ABC):
    def setup(self):  # Concrete
        print("Setup")
    
    @abstractmethod
    def run_test(self):  # Abstract
        pass


# Abstract Class : Can have concrete methods, Can have instance variables, Single inheritance
# Interface (Protocol in Python): All methods abstract, Only method signatures, Multiple inheritance

# 4. OOP Concepts in Framework

# 1. ENCAPSULATION - Hide internal details
class LoginPage:
    def __init__(self, driver):
        self.__driver = driver  # Private variable
        self.__username = (By.ID, "user")
    
    def login(self, user, pwd):  # Public method
        self.__driver.find_element(*self.__username).send_keys(user)

# 2. INHERITANCE - Reuse code
class BasePage:
    def __init__(self, driver):
        self.driver = driver
    
    def click(self, locator):
        self.driver.find_element(*locator).click()

class LoginPage(BasePage):  # Inherits click() method
    def login(self):
        self.click((By.ID, "submit"))

# 3. POLYMORPHISM - Same method, different behavior
class BasePage:
    def verify_page(self):
        pass

class LoginPage(BasePage):
    def verify_page(self):
        assert "Login" in self.driver.title

class DashboardPage(BasePage):
    def verify_page(self):
        assert "Dashboard" in self.driver.title

# 4. ABSTRACTION - Hide complexity
from abc import ABC, abstractmethod

class TestBase(ABC):
    @abstractmethod
    def setup_test(self):
        pass
    
    def run_test(self):
        self.setup_test()
        # Common test logic


# Your Interview Answer:

# "In my Atlas automation framework:

# Encapsulation: Page objects hide locators and expose only methods
# Inheritance: All pages inherit from BasePage for common actions (click, wait)
# Polymorphism: Different validate() methods for different pages
# Abstraction: Abstract BaseTest class defines test lifecycle, child tests implement specific validation"
