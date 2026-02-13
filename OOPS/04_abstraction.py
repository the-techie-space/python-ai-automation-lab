"""
Object-Oriented Programming - Abstraction
==========================================
Learn abstract classes, abstract methods, and hiding complexity
"""

from abc import ABC, abstractmethod

# ============================================================================
# ABSTRACTION - What and Why?
# ============================================================================
"""
Abstraction = Hiding implementation details, showing only essential features

Goals:
- Hide complexity
- Show only what's necessary
- Define contract/interface
- Force child classes to implement methods

Real-world analogy:
    Car:
    - Interface: Steering wheel, pedals, gears
    - Hidden: Engine mechanics, fuel injection, transmission
    You don't need to know HOW engine works to drive!

Python Implementation:
- Abstract Base Class (ABC)
- Abstract methods (@abstractmethod)
"""

print("="*60)
print("ABSTRACTION - Concept")
print("="*60)

# ============================================================================
# ABSTRACT BASE CLASS (ABC)
# ============================================================================
"""
Abstract Base Class (ABC):
- Cannot be instantiated directly
- Contains abstract methods (blueprint)
- May contain concrete methods (implemented)
- Child classes MUST implement abstract methods

Syntax:
    from abc import ABC, abstractmethod
    
    class MyAbstractClass(ABC):
        @abstractmethod
        def my_method(self):
            pass
"""

print("\n" + "="*60)
print("ABSTRACT BASE CLASS")
print("="*60)

class Animal(ABC):
    """Abstract Animal class"""
    
    def __init__(self, name):
        self.name = name
    
    # Abstract method - MUST be implemented by child
    @abstractmethod
    def sound(self):
        """Each animal makes different sound"""
        pass
    
    # Concrete method - inherited by all children
    def sleep(self):
        """All animals sleep the same way"""
        print(f"{self.name} is sleeping")

# Cannot create instance of abstract class!
print("\n--- Trying to instantiate abstract class ---")
try:
    animal = Animal("Generic")  # ✗ TypeError!
except TypeError as e:
    print(f"Error: {e}")
    print("Cannot instantiate abstract class!")

# Child classes MUST implement abstract methods
class Dog(Animal):
    """Concrete Dog class"""
    
    def sound(self):
        """Must implement this!"""
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    """Concrete Cat class"""
    
    def sound(self):
        """Must implement this!"""
        print(f"{self.name} says: Meow!")

# Now we can create instances
print("\n--- Creating concrete instances ---")
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.sound()   # Implemented method
dog.sleep()   # Inherited method

cat.sound()   # Implemented method
cat.sleep()   # Inherited method

# ============================================================================
# ABSTRACT CLASS vs CONCRETE CLASS
# ============================================================================
print("\n" + "="*60)
print("ABSTRACT vs CONCRETE CLASSES")
print("="*60)

comparison = """
ABSTRACT CLASS:
✓ Contains @abstractmethod
✓ Cannot be instantiated
✓ Serves as blueprint
✓ Child MUST implement abstract methods
✗ Cannot create objects directly

CONCRETE CLASS:
✓ No abstract methods (or all implemented)
✓ Can be instantiated
✓ Fully implemented
✓ Ready to use
"""
print(comparison)

# ============================================================================
# ABSTRACT METHODS vs CONCRETE METHODS
# ============================================================================
print("\n" + "="*60)
print("ABSTRACT vs CONCRETE METHODS")
print("="*60)

class Vehicle(ABC):
    """Vehicle with both abstract and concrete methods"""
    
    def __init__(self, brand):
        self.brand = brand
    
    # Abstract method - child must implement
    @abstractmethod
    def start_engine(self):
        """Each vehicle starts differently"""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """Each vehicle stops differently"""
        pass
    
    # Concrete method - shared implementation
    def display_info(self):
        """All vehicles display info the same way"""
        print(f"Brand: {self.brand}")
    
    # Concrete method with common logic
    def honk(self):
        """All vehicles honk"""
        print(f"{self.brand} says: Beep beep!")

class Car(Vehicle):
    """Car implements all abstract methods"""
    
    def start_engine(self):
        print(f"{self.brand} car: Turn key to start")
    
    def stop_engine(self):
        print(f"{self.brand} car: Turn key to stop")

class Motorcycle(Vehicle):
    """Motorcycle implements all abstract methods"""
    
    def start_engine(self):
        print(f"{self.brand} motorcycle: Press start button")
    
    def stop_engine(self):
        print(f"{self.brand} motorcycle: Press kill switch")

# Create vehicles
print("\n--- Using concrete classes ---")
car = Car("Toyota")
bike = Motorcycle("Harley")

car.start_engine()    # Implemented
car.display_info()    # Inherited
car.honk()            # Inherited

bike.start_engine()   # Implemented
bike.display_info()   # Inherited
bike.honk()           # Inherited

# ============================================================================
# INTERFACE vs ABSTRACT CLASS (Python Perspective)
# ============================================================================
"""
Python doesn't have 'interface' keyword like Java/C#

But we can create interface-like classes:
- All methods are abstract
- No implementation

vs

Abstract Class:
- Mix of abstract and concrete methods
- Can have instance variables
"""

print("\n" + "="*60)
print("INTERFACE-LIKE vs ABSTRACT CLASS")
print("="*60)

# Interface-like (all methods abstract)
class IDatabase(ABC):
    """Interface: All methods abstract"""
    
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass
    
    @abstractmethod
    def close(self):
        pass

# Abstract class (mix of abstract and concrete)
class BaseDatabase(ABC):
    """Abstract class: Mix of methods"""
    
    def __init__(self, host):
        self.host = host
    
    # Concrete method
    def log(self, message):
        print(f"[{self.host}] {message}")
    
    # Abstract methods
    @abstractmethod
    def connect(self):
        pass
    
    @abstractmethod
    def execute_query(self, query):
        pass

# Implementing interface-like class
class MySQL(IDatabase):
    """MySQL implements IDatabase"""
    
    def connect(self):
        print("Connecting to MySQL")
    
    def execute_query(self, query):
        print(f"MySQL executing: {query}")
    
    def close(self):
        print("Closing MySQL connection")

# Implementing abstract class
class PostgreSQL(BaseDatabase):
    """PostgreSQL extends BaseDatabase"""
    
    def connect(self):
        self.log("Connecting to PostgreSQL")
    
    def execute_query(self, query):
        self.log(f"Executing: {query}")

# Usage
print("\n--- Interface-like implementation ---")
mysql = MySQL()
mysql.connect()
mysql.execute_query("SELECT * FROM users")
mysql.close()

print("\n--- Abstract class implementation ---")
postgres = PostgreSQL("localhost")
postgres.connect()
postgres.execute_query("SELECT * FROM products")

# ============================================================================
# ABSTRACTION IN TEST AUTOMATION
# ============================================================================
print("\n" + "="*60)
print("ABSTRACTION IN TEST AUTOMATION")
print("="*60)

class BasePage(ABC):
    """Abstract base page for Page Object Model"""
    
    def __init__(self, driver):
        self.driver = driver
    
    # Concrete methods - common to all pages
    def click_element(self, locator):
        """Common click implementation"""
        print(f"Clicking: {locator}")
        # self.driver.find_element(*locator).click()
    
    def enter_text(self, locator, text):
        """Common text entry"""
        print(f"Entering '{text}' in: {locator}")
        # self.driver.find_element(*locator).send_keys(text)
    
    def wait_for_element(self, locator, timeout=10):
        """Common wait"""
        print(f"Waiting for: {locator}")
    
    # Abstract method - each page implements differently
    @abstractmethod
    def verify_page_loaded(self):
        """Each page verifies differently"""
        pass
    
    @abstractmethod
    def get_page_title(self):
        """Each page has different title"""
        pass

# Concrete page implementations
class LoginPage(BasePage):
    """Login page implementation"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = ("id", "username")
        self.password_field = ("id", "password")
        self.submit_button = ("id", "submit")
    
    def verify_page_loaded(self):
        """Verify login page"""
        print("Verifying login page loaded")
        print("  Checking for username field")
        print("  Checking for password field")
        return True
    
    def get_page_title(self):
        """Get login page title"""
        return "Login - MyApp"
    
    def login(self, username, password):
        """Login using inherited methods"""
        self.enter_text(self.username_field, username)
        self.enter_text(self.password_field, password)
        self.click_element(self.submit_button)

class DashboardPage(BasePage):
    """Dashboard page implementation"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.welcome_message = ("id", "welcome")
        self.logout_button = ("id", "logout")
    
    def verify_page_loaded(self):
        """Verify dashboard page"""
        print("Verifying dashboard page loaded")
        print("  Checking for welcome message")
        print("  Checking for logout button")
        return True
    
    def get_page_title(self):
        """Get dashboard page title"""
        return "Dashboard - MyApp"
    
    def logout(self):
        """Logout"""
        self.click_element(self.logout_button)

# Usage in tests
print("\n--- Using Page Objects ---")
driver = "MockDriver"

login_page = LoginPage(driver)
print(f"\nPage: {login_page.get_page_title()}")
login_page.verify_page_loaded()
login_page.login("testuser", "password123")

dashboard = DashboardPage(driver)
print(f"\nPage: {dashboard.get_page_title()}")
dashboard.verify_page_loaded()
dashboard.logout()

# ============================================================================
# MULTIPLE ABSTRACT METHODS
# ============================================================================
print("\n" + "="*60)
print("MULTIPLE ABSTRACT METHODS")
print("="*60)

class Shape(ABC):
    """Abstract Shape class"""
    
    @abstractmethod
    def area(self):
        """Calculate area"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate perimeter"""
        pass
    
    def display(self):
        """Concrete method"""
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

class Rectangle(Shape):
    """Rectangle implements Shape"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """Circle implements Shape"""
    
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14159
    
    def area(self):
        return self.pi * self.radius * self.radius
    
    def perimeter(self):
        return 2 * self.pi * self.radius

# Usage
print("\n--- Shape calculations ---")
rect = Rectangle(5, 3)
print("Rectangle (5 x 3):")
rect.display()

circle = Circle(4)
print("\nCircle (radius 4):")
circle.display()

# ============================================================================
# ABSTRACTION vs ENCAPSULATION
# ============================================================================
print("\n" + "="*60)
print("ABSTRACTION vs ENCAPSULATION")
print("="*60)

comparison = """
ABSTRACTION:
✓ WHAT to do (interface/contract)
✓ Hide complexity
✓ Define structure
✓ Use: Abstract classes, abstract methods
Example: Animal.sound() - WHAT to implement

ENCAPSULATION:
✓ HOW to protect data
✓ Hide data
✓ Control access
✓ Use: Private variables, getters/setters
Example: __balance - HOW to protect

BOTH WORK TOGETHER:
- Abstraction: Define what methods exist
- Encapsulation: Hide how data is stored/accessed
"""
print(comparison)

# ============================================================================
# PRACTICAL EXAMPLE: Test Framework Base
# ============================================================================
print("\n" + "="*60)
print("PRACTICAL: Test Framework Base Class")
print("="*60)

class BaseTest(ABC):
    """Abstract base test class"""
    
    def run(self):
        """Template method - concrete"""
        print("\n" + "="*50)
        print(f"Running test: {self.__class__.__name__}")
        print("="*50)
        
        self.setup()
        try:
            self.execute_test()
            self.verify_results()
            print("✓ Test PASSED")
        except AssertionError as e:
            print(f"✗ Test FAILED: {e}")
        finally:
            self.teardown()
    
    # Concrete methods
    def setup(self):
        """Default setup"""
        print("Setting up test...")
    
    def teardown(self):
        """Default teardown"""
        print("Tearing down test...")
    
    # Abstract methods - child must implement
    @abstractmethod
    def execute_test(self):
        """Execute test steps"""
        pass
    
    @abstractmethod
    def verify_results(self):
        """Verify test results"""
        pass

# Concrete test implementation
class LoginTest(BaseTest):
    """Concrete login test"""
    
    def execute_test(self):
        """Implement test steps"""
        print("1. Navigate to login page")
        print("2. Enter credentials")
        print("3. Click login button")
    
    def verify_results(self):
        """Implement verification"""
        print("Verifying user is logged in")
        print("Checking dashboard is displayed")

class SearchTest(BaseTest):
    """Concrete search test"""
    
    def execute_test(self):
        """Implement test steps"""
        print("1. Enter search query")
        print("2. Click search button")
    
    def verify_results(self):
        """Implement verification"""
        print("Verifying search results displayed")

# Run tests
login_test = LoginTest()
login_test.run()

search_test = SearchTest()
search_test.run()

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
ABSTRACTION:
✓ Hide implementation details
✓ Show only essential features
✓ Define contract/blueprint
✓ Force child implementation

ABSTRACT BASE CLASS:
✓ Inherit from ABC
✓ Cannot be instantiated
✓ Can have concrete and abstract methods
✓ Child must implement abstract methods

@abstractmethod:
✓ Decorator for abstract methods
✓ Method signature only (or pass)
✓ Child MUST implement
✓ Enforces contract

INTERFACE-LIKE (Python):
✓ All methods abstract
✓ No implementation
✓ Pure contract
✓ Use ABC with all @abstractmethod

ABSTRACTION vs ENCAPSULATION:
✓ Abstraction: WHAT to do (hide complexity)
✓ Encapsulation: HOW to protect (hide data)

WHEN TO USE:
✓ Common interface for different implementations
✓ Force structure in framework
✓ Template pattern
✓ Plugin architecture

INTERVIEW ANSWER:
"Abstraction hides implementation complexity and defines contracts.
I use ABC for base classes like BasePage and BaseTest, with 
@abstractmethod for methods each child must implement like 
verify_page_loaded(). This ensures consistent interface across 
all page objects."

REAL-WORLD EXAMPLES:
✓ Payment gateway (PayPal, Stripe - different implementations)
✓ Database drivers (MySQL, PostgreSQL - same interface)
✓ Page objects (Login, Dashboard - common base)
✓ Test framework (setup, execute, verify - template)
"""

print("\n" + "="*60)
print("✓ Abstraction mastered!")
print("="*60)