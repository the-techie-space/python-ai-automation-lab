# Object-Oriented Programming in Python 📚

A comprehensive guide to OOP concepts with practical examples for test automation and real-world applications.

## 📂 File Structure

```
OOP_Python/
├── README.md                          # You are here!
├── 01_basics_classes_objects.py      # Classes, objects, self, __init__, variables
├── 02_inheritance_polymorphism.py    # Code reuse and method overriding
├── 03_encapsulation.py               # Data hiding and access control
├── 04_abstraction.py                 # Abstract classes and methods
└── 05_oop_in_frameworks.py           # Real-world test automation examples
```

## 🎯 Learning Path

### **Beginner** (Start Here)
1. **01_basics_classes_objects.py** - Classes, objects, self, __init__
2. **02_inheritance_polymorphism.py** - Inheritance and method overriding

### **Intermediate**
3. **03_encapsulation.py** - Data hiding with private variables
4. **04_abstraction.py** - Abstract classes and methods

### **Advanced**
5. **05_oop_in_frameworks.py** - Complete framework examples

## 📖 What You'll Learn

### File 1: Basics - Classes & Objects (01_basics_classes_objects.py)
- ✓ What is a class? (Blueprint vs Instance)
- ✓ Understanding 'self' (reference to current object)
- ✓ The __init__ constructor
- ✓ Instance variables vs class variables
- ✓ Types of methods (instance, class, static)
- ✓ Practical example: Bank Account system

### File 2: Inheritance & Polymorphism (02_inheritance_polymorphism.py)
- ✓ Single, multiple, multilevel, hierarchical inheritance
- ✓ Using super() to call parent methods
- ✓ Method overriding (polymorphism)
- ✓ Method Resolution Order (MRO)
- ✓ Duck typing in Python
- ✓ Inheritance vs composition
- ✓ Page Object Model example

### File 3: Encapsulation (03_encapsulation.py)
- ✓ Public, protected, private variables
- ✓ Why encapsulation? (data protection)
- ✓ Getters and setters (2 methods)
- ✓ @property decorator (Pythonic way)
- ✓ Practical examples: Bank account, User authentication
- ✓ Encapsulation in page objects

### File 4: Abstraction (04_abstraction.py)
- ✓ Abstract Base Class (ABC)
- ✓ @abstractmethod decorator
- ✓ Abstract vs concrete classes
- ✓ Interface-like classes in Python
- ✓ Abstract vs concrete methods
- ✓ Abstraction vs encapsulation
- ✓ Test framework base class example

### File 5: OOP in Frameworks (05_oop_in_frameworks.py)
- ✓ Encapsulation in page objects (hide locators)
- ✓ Inheritance in BasePage (code reuse)
- ✓ Polymorphism in page validation
- ✓ Abstraction in BaseTest (enforce structure)
- ✓ Complete framework example
- ✓ Interview answer templates

## 🔥 The Four Pillars of OOP

| Pillar | What | Why | How |
|--------|------|-----|-----|
| **Encapsulation** | Hide data | Protect sensitive info | Private vars, public methods |
| **Inheritance** | Reuse code | DRY principle | class Child(Parent) |
| **Polymorphism** | Same interface | Flexibility | Method overriding |
| **Abstraction** | Hide complexity | Define contracts | ABC, @abstractmethod |

## 💡 Quick Reference

### Class & Object
```python
class Car:
    def __init__(self, brand):
        self.brand = brand  # Instance variable
    
    def drive(self):
        print(f"{self.brand} is driving")

car = Car("Toyota")  # Create object
car.drive()           # Call method
```

### Instance vs Class Variables
```python
class Employee:
    company = "Dell"  # Class variable (shared)
    
    def __init__(self, name):
        self.name = name  # Instance variable (unique)
```

### Inheritance
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof!")
```

### Encapsulation
```python
class Account:
    def __init__(self):
        self.__balance = 0  # Private
    
    def deposit(self, amount):  # Public
        if amount > 0:
            self.__balance += amount
```

### Abstraction
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius ** 2
```

## 🎓 Interview Preparation

### Common Questions

**Q: What is a class and object?**
```
A: Class is a blueprint/template. Object is an instance of a class.
   Example: Class=Car blueprint, Object=My Toyota Camry
```

**Q: What is self?**
```
A: 'self' refers to the current object instance. It's used to:
   - Access instance variables (self.name)
   - Call instance methods (self.method())
   - Required as first parameter in instance methods
```

**Q: What is __init__?**
```
A: Constructor method that initializes object when created.
   Called automatically during object creation.
   Used to set initial values for instance variables.
```

**Q: Explain the four pillars of OOP**
```
A: 
1. Encapsulation: Bundle data + methods, hide implementation
2. Inheritance: Reuse code from parent class
3. Polymorphism: Same method, different behavior
4. Abstraction: Hide complexity, show only essential features
```

**Q: Instance variable vs class variable?**
```
A: Instance variable: Unique to each object (self.name)
   Class variable: Shared by all objects (Company.name)
```

**Q: When to use inheritance vs composition?**
```
A: Inheritance: IS-A relationship (Dog IS-A Animal)
   Composition: HAS-A relationship (Car HAS-A Engine)
```

**Q: How do you use OOP in your framework?**
```
A: (See File 5 for complete answer template)
   - Encapsulation: Hide locators in page objects
   - Inheritance: BasePage for common methods
   - Polymorphism: Different verify_page() per page
   - Abstraction: BaseTest enforces test structure
```

### One-Liner Cheat Sheet
```
Class: Blueprint
Object: Instance of class
__init__: Constructor
self: Refers to current object
Instance variable: Object-specific (self.var)
Class variable: Shared across all objects
Inheritance: Code reuse (class Child(Parent))
Polymorphism: Same method, different behavior
Encapsulation: Data hiding (__private)
Abstraction: Hide implementation (ABC)
```

## 🔍 Practical Examples by Topic

### Banking System (Files 1, 3)
- Account class with balance
- Encapsulated transactions
- Getters and setters
- Input validation

### Vehicle Hierarchy (Files 2, 4)
- Vehicle base class
- Car and Motorcycle inheritance
- Polymorphic start_engine()
- Abstract methods

### Test Automation (File 5)
- BasePage with common actions
- LoginPage, DashboardPage inheritance
- Polymorphic verify_page()
- BaseTest abstract class

## 📝 Best Practices

### Design Principles
1. **Single Responsibility**: One class, one purpose
2. **DRY (Don't Repeat Yourself)**: Use inheritance
3. **KISS (Keep It Simple)**: Don't over-engineer
4. **Encapsulation**: Always use private for sensitive data
5. **Favor Composition over Inheritance**: When appropriate

### Naming Conventions
```python
class ClassName:          # PascalCase for classes
    def method_name(self): # snake_case for methods
        pass
    
    PUBLIC_CONSTANT = 10   # UPPERCASE for constants
    _protected = 1         # _single for protected
    __private = 2          # __double for private
```

### When to Use What

**Use Classes When:**
- Multiple related objects with same structure
- Need to bundle data and behavior
- Want code reusability

**Use Inheritance When:**
- Clear IS-A relationship
- Want to reuse parent functionality
- Shallow hierarchy (2-3 levels)

**Use Composition When:**
- HAS-A relationship
- Need flexibility
- Want loose coupling

## 🚀 Advanced Topics

After mastering basics:
1. **Magic/Dunder Methods**: __str__, __repr__, __eq__
2. **Decorators**: @property, @classmethod, @staticmethod
3. **Context Managers**: __enter__, __exit__
4. **Metaclasses**: Advanced class creation
5. **Design Patterns**: Singleton, Factory, Observer

## 📊 OOP vs Procedural Programming

```
PROCEDURAL:
- Functions and data separate
- Data passed to functions
- Less organized
- Harder to maintain

OOP:
- Data and functions together (class)
- Objects encapsulate both
- Better organization
- Easier to maintain and extend
```

## 🔗 Real-World Applications

### Test Automation Framework
- **Page Objects**: Encapsulation
- **BasePage**: Inheritance
- **Page Verification**: Polymorphism
- **BaseTest**: Abstraction

### Web Development
- **User Model**: Class
- **Admin User**: Inheritance
- **Different Roles**: Polymorphism
- **Database Interface**: Abstraction

### Game Development
- **Character**: Class
- **Warrior/Mage**: Inheritance
- **Attack Method**: Polymorphism
- **GameObject**: Abstraction

## 📚 Additional Resources

### Documentation
- Official Python Docs: https://docs.python.org/3/tutorial/classes.html
- Real Python OOP: https://realpython.com/python3-object-oriented-programming/

### Practice Platforms
- LeetCode: OOP design questions
- HackerRank: Object-oriented programming track
- Exercism: Python track with OOP exercises

## 🎯 Learning Roadmap

### Week 1: Basics
- [ ] Classes and objects
- [ ] __init__ and self
- [ ] Instance vs class variables
- [ ] Practice: Create 3 different classes

### Week 2: Core Concepts
- [ ] Inheritance
- [ ] Polymorphism
- [ ] Encapsulation
- [ ] Practice: Build class hierarchy

### Week 3: Advanced
- [ ] Abstraction
- [ ] @property decorator
- [ ] Practice: Design patterns

### Week 4: Application
- [ ] Page Object Model
- [ ] Test framework design
- [ ] Practice: Build mini framework

## 🤝 Common Mistakes to Avoid

1. **Forgetting self**: Always use self for instance variables
2. **Deep inheritance**: Keep hierarchies shallow (2-3 levels)
3. **God classes**: Don't put everything in one class
4. **Not using encapsulation**: Always protect sensitive data
5. **Overusing inheritance**: Consider composition
6. **Ignoring ABC**: Use for defining interfaces

## ✅ Checklist

- [ ] Can explain class vs object
- [ ] Understand self and __init__
- [ ] Know instance vs class variables
- [ ] Can use inheritance
- [ ] Understand polymorphism
- [ ] Can implement encapsulation
- [ ] Can use abstract classes
- [ ] Can apply OOP in test automation
- [ ] Ready for OOP interviews!

---

## 💬 Quick Interview Answers

**Encapsulation:**
*"Bundling data with methods and restricting direct access. Use private variables with public methods."*

**Inheritance:**
*"Child class inherits from parent. Promotes code reuse. Example: BasePage in my framework."*

**Polymorphism:**
*"Same method name, different implementation. Each page has verify_page() but different logic."*

**Abstraction:**
*"Hide complexity, define contracts. Use ABC with @abstractmethod. BaseTest in my framework."*

---

**Happy Learning! 🎉**

*Master OOP and you'll write cleaner, more maintainable code for any project!*