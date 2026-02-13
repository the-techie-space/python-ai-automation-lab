"""
Object-Oriented Programming - Inheritance & Polymorphism
=========================================================
Learn code reuse and method overriding
"""

# ============================================================================
# INHERITANCE - Code Reuse
# ============================================================================
"""
Inheritance = One class (child) inherits properties and methods 
             from another class (parent)

Benefits:
- Code reuse (don't repeat yourself)
- Logical hierarchy
- Easy maintenance
- Extensibility

Terminology:
- Parent/Base/Super class
- Child/Derived/Sub class

Syntax:
    class Child(Parent):
        pass
"""

print("="*60)
print("INHERITANCE - Basic Concept")
print("="*60)

# Parent class
class Animal:
    """Base Animal class"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

# Child class inherits from Animal
class Dog(Animal):
    """Dog inherits from Animal"""
    
    def bark(self):
        print(f"{self.name} barks: Woof!")

# Create dog object
print("\n--- Dog (inherits from Animal) ---")
d = Dog("Buddy")
d.speak()  # Inherited from Animal
d.sleep()  # Inherited from Animal
d.bark()   # Own method

# ============================================================================
# INHERITANCE WITH __init__
# ============================================================================
"""
When child has __init__, it OVERRIDES parent's __init__
To call parent's __init__, use:
- super().__init__() (recommended)
- ParentClass.__init__(self)
"""

print("\n" + "="*60)
print("INHERITANCE with Constructor")
print("="*60)

class Vehicle:
    """Parent Vehicle class"""
    
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        print(f"Vehicle created: {brand} {model}")
    
    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class Car(Vehicle):
    """Child Car class"""
    
    def __init__(self, brand, model, doors):
        # Call parent constructor
        super().__init__(brand, model)
        self.doors = doors
        print(f"Car created with {doors} doors")
    
    def car_info(self):
        print(f"{self.brand} {self.model} - {self.doors} doors")

# Create car
print("\n--- Creating Car ---")
c = Car("Toyota", "Camry", 4)
c.info()      # Inherited method
c.car_info()  # Own method

# ============================================================================
# TYPES OF INHERITANCE
# ============================================================================
"""
1. Single Inheritance: Child → Parent
2. Multiple Inheritance: Child → Parent1, Parent2
3. Multilevel Inheritance: GrandChild → Child → Parent
4. Hierarchical: Multiple children from one parent
"""

print("\n" + "="*60)
print("TYPES OF INHERITANCE")
print("="*60)

# 1. Single Inheritance (already shown above)
print("\n1. Single Inheritance: Dog → Animal")

# 2. Multiple Inheritance
print("\n2. Multiple Inheritance:")

class Flyer:
    def fly(self):
        print("Flying in the sky")

class Swimmer:
    def swim(self):
        print("Swimming in water")

class Duck(Flyer, Swimmer):  # Inherits from both
    def quack(self):
        print("Quack quack!")

duck = Duck()
duck.fly()   # From Flyer
duck.swim()  # From Swimmer
duck.quack() # Own method

# 3. Multilevel Inheritance
print("\n3. Multilevel Inheritance:")

class LivingBeing:
    def breathe(self):
        print("Breathing...")

class Mammal(LivingBeing):
    def feed_milk(self):
        print("Feeding milk to babies")

class Human(Mammal):
    def think(self):
        print("Thinking...")

person = Human()
person.breathe()    # From LivingBeing
person.feed_milk()  # From Mammal
person.think()      # Own method

# 4. Hierarchical Inheritance
print("\n4. Hierarchical Inheritance:")

class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def draw(self):
        print(f"Drawing {self.color} circle")

class Square(Shape):
    def draw(self):
        print(f"Drawing {self.color} square")

circle = Circle("red")
square = Square("blue")
circle.draw()
square.draw()

# ============================================================================
# POLYMORPHISM - Same Method, Different Behavior
# ============================================================================
"""
Polymorphism = "Many forms"

Same method name, different implementations in different classes

Achieved via:
- Method Overriding (child redefines parent method)
- Duck Typing (if it walks like a duck...)

Benefits:
- Flexibility
- Code extensibility
- Clean interface
"""

print("\n" + "="*60)
print("POLYMORPHISM - Method Overriding")
print("="*60)

class Bird:
    """Parent Bird class"""
    
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print(f"{self.name} makes a sound")

class Sparrow(Bird):
    """Child class - overrides sound()"""
    
    def sound(self):
        print(f"{self.name} says: Chirp chirp!")

class Crow(Bird):
    """Child class - overrides sound()"""
    
    def sound(self):
        print(f"{self.name} says: Caw caw!")

# Polymorphism in action
print("\n--- Same method, different behavior ---")
birds = [
    Sparrow("Tweety"),
    Crow("Blacky"),
    Bird("Generic Bird")
]

for bird in birds:
    bird.sound()  # Each calls their own version!

# ============================================================================
# POLYMORPHISM WITH DIFFERENT CLASSES
# ============================================================================
print("\n" + "="*60)
print("POLYMORPHISM - Duck Typing")
print("="*60)

# Different classes, same method name
class Dog:
    def speak(self):
        print("Dog: Woof!")

class Cat:
    def speak(self):
        print("Cat: Meow!")

class Cow:
    def speak(self):
        print("Cow: Moo!")

# Polymorphic function
def make_animal_speak(animal):
    """Works with any object that has speak() method"""
    animal.speak()

# Works with different classes!
print("\n--- Polymorphic function ---")
make_animal_speak(Dog())
make_animal_speak(Cat())
make_animal_speak(Cow())

# ============================================================================
# METHOD RESOLUTION ORDER (MRO)
# ============================================================================
"""
When multiple inheritance is used, Python follows MRO to find methods

MRO = Left to right, depth-first

View MRO: ClassName.__mro__ or ClassName.mro()
"""

print("\n" + "="*60)
print("METHOD RESOLUTION ORDER (MRO)")
print("="*60)

class A:
    def show(self):
        print("A's show()")

class B(A):
    def show(self):
        print("B's show()")

class C(A):
    def show(self):
        print("C's show()")

class D(B, C):
    pass

# Which show() is called?
d = D()
d.show()  # Calls B's show() (MRO: D → B → C → A)

print(f"\nMRO for class D: {D.__mro__}")

# ============================================================================
# SUPER() - Calling Parent Methods
# ============================================================================
"""
super() = Call parent class methods

Uses:
- Call parent __init__
- Extend parent method (not just override)
- Work with multiple inheritance (follows MRO)
"""

print("\n" + "="*60)
print("USING super()")
print("="*60)

class Employee:
    """Parent Employee class"""
    
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
    
    def work(self):
        print(f"{self.name} is working")

class Manager(Employee):
    """Child Manager class"""
    
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)  # Call parent __init__
        self.department = department
    
    def work(self):
        super().work()  # Call parent work()
        print(f"{self.name} is managing {self.department}")

# Create manager
print("\n--- Manager (extends Employee) ---")
m = Manager("Alice", "E001", "Engineering")
m.work()

# ============================================================================
# PRACTICAL EXAMPLE: Page Object Model (Test Automation)
# ============================================================================
print("\n" + "="*60)
print("PRACTICAL EXAMPLE: Page Object Model")
print("="*60)

class BasePage:
    """Base page with common methods"""
    
    def __init__(self, driver):
        self.driver = driver
    
    def click_element(self, locator):
        print(f"Clicking element: {locator}")
        # self.driver.find_element(*locator).click()
    
    def enter_text(self, locator, text):
        print(f"Entering '{text}' in {locator}")
        # self.driver.find_element(*locator).send_keys(text)
    
    def verify_page(self):
        """Override in child classes"""
        pass

class LoginPage(BasePage):
    """Login page inherits from BasePage"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = ("id", "username")
        self.password_field = ("id", "password")
        self.login_button = ("id", "submit")
    
    def login(self, username, password):
        """Login using inherited methods"""
        self.enter_text(self.username_field, username)
        self.enter_text(self.password_field, password)
        self.click_element(self.login_button)
    
    def verify_page(self):
        """Override parent method"""
        print("Verifying Login page title")

class DashboardPage(BasePage):
    """Dashboard page inherits from BasePage"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.profile_link = ("id", "profile")
        self.logout_button = ("id", "logout")
    
    def go_to_profile(self):
        self.click_element(self.profile_link)
    
    def verify_page(self):
        """Override parent method"""
        print("Verifying Dashboard page title")

# Simulate usage
print("\n--- Using Page Objects ---")
driver = "MockDriver"  # Placeholder

login_page = LoginPage(driver)
login_page.verify_page()  # Polymorphism
login_page.login("testuser", "password123")

dashboard = DashboardPage(driver)
dashboard.verify_page()  # Polymorphism
dashboard.go_to_profile()

# ============================================================================
# INHERITANCE vs COMPOSITION
# ============================================================================
print("\n" + "="*60)
print("INHERITANCE vs COMPOSITION")
print("="*60)

comparison = """
INHERITANCE (IS-A relationship):
✓ Dog IS-A Animal
✓ Car IS-A Vehicle
✗ Tight coupling
✗ Changes in parent affect all children

COMPOSITION (HAS-A relationship):
✓ Car HAS-A Engine
✓ Person HAS-A Address
✓ Loose coupling
✓ More flexible

WHEN TO USE:
- Inheritance: Clear IS-A relationship, shared behavior
- Composition: HAS-A relationship, flexible combinations
"""
print(comparison)

# Composition example
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # HAS-A Engine
    
    def start(self):
        self.engine.start()
        print("Car is ready")

car = Car()
car.start()

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
INHERITANCE:
✓ Code reuse - child inherits from parent
✓ Syntax: class Child(Parent):
✓ super() to call parent methods
✓ Types: Single, Multiple, Multilevel, Hierarchical

POLYMORPHISM:
✓ Same method, different behavior
✓ Method overriding in child classes
✓ Duck typing - if it quacks like a duck...
✓ Enables flexible, extensible code

METHOD RESOLUTION ORDER:
✓ Determines which method is called
✓ Left to right, depth-first
✓ Check with ClassName.__mro__

super():
✓ Call parent class methods
✓ Works with single and multiple inheritance
✓ Follows MRO automatically

BEST PRACTICES:
✓ Use inheritance for IS-A relationships
✓ Use composition for HAS-A relationships
✓ Override methods for polymorphism
✓ Call super().__init__() in child constructors
✓ Keep inheritance hierarchies shallow (2-3 levels)

INTERVIEW TIPS:
✓ Explain inheritance for code reuse
✓ Give polymorphism examples (method overriding)
✓ Mention super() for calling parent methods
✓ Know when to use inheritance vs composition
"""

print("\n" + "="*60)
print("✓ Inheritance & Polymorphism mastered!")
print("="*60)