"""
Object-Oriented Programming - Basics
=====================================
Core concepts: Classes, Objects, __init__, self, Variables
"""

# ============================================================================
# WHAT IS A CLASS?
# ============================================================================
"""
Class = Blueprint or template that defines:
- Properties (variables/attributes)
- Behaviors (methods/functions)

Object = Instance of a class (real-world entity)

Analogy:
    Class = Car blueprint
    Object = Your actual car (Toyota Camry 2024)
"""

print("="*60)
print("CLASSES AND OBJECTS")
print("="*60)

# Simple class example
class Car:
    """A simple Car class"""
    
    def drive(self):
        print("Car is driving")

# Creating objects (instances)
c1 = Car()  # object 1
c2 = Car()  # object 2

print("\nCalling drive() method:")
c1.drive()  # Car is driving
c2.drive()  # Car is driving

print("\nKey concept: Class = blueprint, Object = real-world instance")

# ============================================================================
# WHAT IS 'self'?
# ============================================================================
"""
self = Reference to the current object/instance

Purpose:
- Access instance variables (self.name, self.age)
- Call instance methods (self.method_name())
- Differentiate instance data from local variables

CRITICAL: Without 'self', instance variables won't work!
"""

print("\n" + "="*60)
print("UNDERSTANDING 'self'")
print("="*60)

class Dog:
    def __init__(self, name):
        self.name = name  # Instance variable
    
    def bark(self):
        # 'self' refers to the current object
        print(f"{self.name} says: Woof!")
    
    def get_name(self):
        return self.name  # Access via self

# Create objects
dog1 = Dog("Buddy")
dog2 = Dog("Max")

print("\nEach object has its own data:")
dog1.bark()  # Buddy says: Woof!
dog2.bark()  # Max says: Woof!

print(f"\ndog1.name = {dog1.get_name()}")
print(f"dog2.name = {dog2.get_name()}")

# ============================================================================
# THE __init__ METHOD (Constructor)
# ============================================================================
"""
__init__ = Constructor method

Key Points:
- Automatically called when object is created
- Used to initialize object data (instance variables)
- First parameter is always 'self'
- Can have additional parameters

Syntax:
    def __init__(self, param1, param2):
        self.attribute1 = param1
        self.attribute2 = param2
"""

print("\n" + "="*60)
print("THE __init__ CONSTRUCTOR")
print("="*60)

class Person:
    """Person class with constructor"""
    
    def __init__(self, name, age):
        """Initialize person with name and age"""
        self.name = name  # Instance variable
        self.age = age    # Instance variable
        print(f"Created person: {name}, {age} years old")
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")

# Object creation - __init__ is called automatically
print("\nCreating objects:")
p1 = Person("Alice", 30)
p2 = Person("Bob", 25)

print("\nCalling methods:")
p1.introduce()
p2.introduce()

# ============================================================================
# INSTANCE VARIABLES vs CLASS VARIABLES
# ============================================================================
"""
Instance Variables:
- Belong to each object individually
- Defined using 'self' in __init__ or methods
- Each object has its own copy
- Access: self.variable_name

Class Variables:
- Shared across ALL objects of the class
- Defined inside class but outside methods
- Same value for all instances
- Access: ClassName.variable_name or self.variable_name
"""

print("\n" + "="*60)
print("INSTANCE vs CLASS VARIABLES")
print("="*60)

class Employee:
    """Employee class demonstrating both variable types"""
    
    # Class variable (shared by all employees)
    company = "Dell"
    employee_count = 0
    
    def __init__(self, name, salary):
        # Instance variables (unique to each employee)
        self.name = name
        self.salary = salary
        
        # Increment class variable
        Employee.employee_count += 1
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Company: {self.company}")

# Create employees
e1 = Employee("John", 50000)
e2 = Employee("Emma", 60000)
e3 = Employee("Mike", 55000)

print("\nEmployee 1:")
e1.display_info()

print("\nEmployee 2:")
e2.display_info()

print(f"\nTotal employees: {Employee.employee_count}")
print(f"Company name (via class): {Employee.company}")
print(f"Company name (via e1): {e1.company}")
print(f"Company name (via e2): {e2.company}")

# Changing class variable
print("\n--- Changing company name ---")
Employee.company = "Microsoft"
print(f"e1.company: {e1.company}")  # Microsoft
print(f"e2.company: {e2.company}")  # Microsoft
print(f"e3.company: {e3.company}")  # Microsoft

# Instance variable vs class variable name collision
print("\n--- Instance override ---")
e1.company = "Google"  # Creates instance variable!
print(f"e1.company: {e1.company}")           # Google (instance)
print(f"e2.company: {e2.company}")           # Microsoft (class)
print(f"Employee.company: {Employee.company}")  # Microsoft (class)

# ============================================================================
# METHODS - Instance, Class, and Static
# ============================================================================
"""
Instance Methods:
- Operate on instance data
- First parameter: self
- Can access and modify instance variables

Class Methods:
- Operate on class data
- First parameter: cls
- Decorator: @classmethod

Static Methods:
- Don't access instance or class data
- Utility functions
- Decorator: @staticmethod
"""

print("\n" + "="*60)
print("TYPES OF METHODS")
print("="*60)

class Calculator:
    """Demonstrates different method types"""
    
    pi = 3.14159  # Class variable
    
    def __init__(self, name):
        self.name = name  # Instance variable
    
    # Instance method
    def add(self, a, b):
        """Regular instance method"""
        return a + b
    
    # Class method
    @classmethod
    def circle_area(cls, radius):
        """Class method - uses class variable"""
        return cls.pi * radius * radius
    
    # Static method
    @staticmethod
    def is_even(num):
        """Static method - utility function"""
        return num % 2 == 0

# Using different method types
calc = Calculator("MyCalc")

# Instance method (needs object)
print(f"Instance method: 5 + 3 = {calc.add(5, 3)}")

# Class method (can call on class or object)
print(f"Class method: Circle area (r=5) = {Calculator.circle_area(5)}")
print(f"Class method via object: {calc.circle_area(5)}")

# Static method (can call on class or object)
print(f"Static method: Is 4 even? {Calculator.is_even(4)}")
print(f"Static method via object: {calc.is_even(7)}")

# ============================================================================
# PRACTICAL EXAMPLE: Bank Account
# ============================================================================
print("\n" + "="*60)
print("PRACTICAL EXAMPLE: Bank Account")
print("="*60)

class BankAccount:
    """Comprehensive bank account example"""
    
    # Class variable
    bank_name = "Python Bank"
    total_accounts = 0
    
    def __init__(self, account_holder, initial_balance=0):
        """Initialize bank account"""
        # Instance variables
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = BankAccount.total_accounts + 1
        
        # Update class variable
        BankAccount.total_accounts += 1
        
        print(f"Account created for {account_holder}")
        print(f"Account #: {self.account_number}")
        print(f"Initial balance: ${self.balance}")
    
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount):
        """Withdraw money"""
        if amount > self.balance:
            print("Insufficient funds")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount")
    
    def get_balance(self):
        """Check balance"""
        return self.balance
    
    def display_info(self):
        """Display account information"""
        print(f"\n{BankAccount.bank_name}")
        print(f"Account #: {self.account_number}")
        print(f"Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

# Create accounts
print("\n--- Creating Accounts ---")
acc1 = BankAccount("Alice", 1000)
acc2 = BankAccount("Bob", 500)

# Perform operations
print("\n--- Transactions ---")
acc1.deposit(500)
acc1.withdraw(200)

acc2.deposit(300)
acc2.withdraw(1000)  # Insufficient funds

# Display information
acc1.display_info()
acc2.display_info()

print(f"\nTotal accounts created: {BankAccount.total_accounts}")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
CLASS:
✓ Blueprint/template for creating objects
✓ Defines attributes and methods
✓ Syntax: class ClassName:

OBJECT:
✓ Instance of a class
✓ Creation: obj = ClassName()
✓ Each object has its own data

self:
✓ Refers to current object
✓ Required for instance variables and methods
✓ Always first parameter in instance methods

__init__:
✓ Constructor - initializes object
✓ Called automatically on object creation
✓ Used to set initial values

INSTANCE VARIABLES:
✓ Unique to each object
✓ Defined with self.variable_name
✓ Each object has its own copy

CLASS VARIABLES:
✓ Shared by all objects
✓ Defined in class body (outside methods)
✓ Same value for all instances

METHODS:
✓ Instance: Operate on object data (self)
✓ Class: Operate on class data (@classmethod, cls)
✓ Static: Utility functions (@staticmethod)

WHEN TO USE:
✓ Classes: When you have multiple related objects
✓ Instance vars: Object-specific data (name, age)
✓ Class vars: Shared data (company, count)
"""

print("\n" + "="*60)
print("✓ OOP Basics mastered!")
print("="*60)