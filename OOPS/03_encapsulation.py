"""
Object-Oriented Programming - Encapsulation
============================================
Learn data hiding and access control
"""

# ============================================================================
# ENCAPSULATION - What and Why?
# ============================================================================
"""
Encapsulation = Bundling data and methods together + restricting access

Goals:
- Protect sensitive data
- Control how data is accessed/modified
- Hide implementation details
- Prevent accidental modifications

Real-world analogy:
    ATM machine:
    - Internal mechanism is hidden
    - You interact via interface (buttons)
    - Can't directly access cash storage
"""

print("="*60)
print("ENCAPSULATION - Concept")
print("="*60)

# ============================================================================
# ACCESS MODIFIERS IN PYTHON
# ============================================================================
"""
Python Access Modifiers:

1. PUBLIC (var)
   - Accessible anywhere
   - No restrictions

2. PROTECTED (_var)
   - Convention: Internal use
   - Still accessible (Python doesn't enforce)
   - Single underscore prefix

3. PRIVATE (__var)
   - Name mangling applied
   - Cannot access directly from outside
   - Double underscore prefix

Note: Python doesn't have true private (unlike Java/C++)
      It's more about convention and name mangling
"""

print("\n" + "="*60)
print("ACCESS MODIFIERS")
print("="*60)

class Example:
    """Demonstrates all access modifiers"""
    
    def __init__(self):
        self.public = "I'm public"           # Public
        self._protected = "I'm protected"    # Protected (convention)
        self.__private = "I'm private"       # Private (name mangling)
    
    def show_all(self):
        """Can access all variables inside the class"""
        print(f"Public: {self.public}")
        print(f"Protected: {self._protected}")
        print(f"Private: {self.__private}")

# Create object
obj = Example()

# Accessing variables
print("\n--- Accessing from outside ---")
print(f"Public: {obj.public}")           # ✓ Works
print(f"Protected: {obj._protected}")    # ✓ Works (but shouldn't per convention)
# print(obj.__private)                   # ✗ AttributeError!

# Accessing private with name mangling
print(f"Private (via mangling): {obj._Example__private}")  # ✓ Works (hacky!)

# Using method
print("\n--- Accessing via method ---")
obj.show_all()

# ============================================================================
# ENCAPSULATION - PRACTICAL EXAMPLE
# ============================================================================
"""
Best Practice: Private variables + Public methods (getters/setters)

Why?
- Validation before setting
- Control over access
- Can change implementation without breaking code
"""

print("\n" + "="*60)
print("ENCAPSULATION - Bank Account Example")
print("="*60)

class BankAccount:
    """Bank account with encapsulated balance"""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Public
        self.__balance = initial_balance      # Private
    
    # Public method to deposit (with validation)
    def deposit(self, amount):
        """Deposit money - validated"""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
            print(f"New balance: ${self.__balance}")
        else:
            print("Error: Deposit amount must be positive")
    
    # Public method to withdraw (with validation)
    def withdraw(self, amount):
        """Withdraw money - validated"""
        if amount <= 0:
            print("Error: Withdrawal amount must be positive")
        elif amount > self.__balance:
            print("Error: Insufficient funds")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}")
            print(f"New balance: ${self.__balance}")
    
    # Public method to get balance (getter)
    def get_balance(self):
        """Get current balance"""
        return self.__balance
    
    # Public method to show details
    def show_details(self):
        """Display account details"""
        print(f"\nAccount Holder: {self.account_holder}")
        print(f"Balance: ${self.__balance}")

# Create account
print("\n--- Creating Account ---")
acc = BankAccount("Alice", 1000)

# Try to access balance directly
print("\n--- Attempting Direct Access ---")
# print(acc.__balance)  # ✗ AttributeError!
print("Cannot access __balance directly!")

# Use public methods (encapsulated access)
print("\n--- Using Public Methods ---")
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)  # Insufficient funds
print(f"\nCurrent balance: ${acc.get_balance()}")

acc.show_details()

# ============================================================================
# GETTERS AND SETTERS
# ============================================================================
"""
Getters and Setters:
- Getter: Method to read private variable
- Setter: Method to modify private variable (with validation)

Python ways:
1. Regular methods (get_x, set_x)
2. @property decorator (Pythonic way)
"""

print("\n" + "="*60)
print("GETTERS AND SETTERS")
print("="*60)

# Method 1: Regular methods
class Person:
    """Using regular getter/setter methods"""
    
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    # Getter
    def get_name(self):
        return self.__name
    
    # Setter with validation
    def set_age(self, age):
        if age > 0 and age < 150:
            self.__age = age
        else:
            print("Invalid age")
    
    # Getter
    def get_age(self):
        return self.__age

print("\n--- Regular Getters/Setters ---")
person = Person("Bob", 30)
print(f"Name: {person.get_name()}")
print(f"Age: {person.get_age()}")

person.set_age(35)
print(f"Updated age: {person.get_age()}")

person.set_age(200)  # Invalid

# Method 2: Using @property (Pythonic!)
class Employee:
    """Using @property decorator"""
    
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    # Getter using @property
    @property
    def name(self):
        """Get name"""
        return self.__name
    
    @property
    def salary(self):
        """Get salary"""
        return self.__salary
    
    # Setter using @property_name.setter
    @salary.setter
    def salary(self, value):
        """Set salary with validation"""
        if value >= 0:
            self.__salary = value
        else:
            print("Salary cannot be negative")
    
    # Read-only property (no setter)
    @property
    def annual_salary(self):
        """Calculated property"""
        return self.__salary * 12

print("\n--- Using @property ---")
emp = Employee("Charlie", 5000)

# Access like attributes (but they're methods!)
print(f"Name: {emp.name}")          # Calls name() getter
print(f"Salary: ${emp.salary}")     # Calls salary() getter

# Set using assignment
emp.salary = 6000                    # Calls salary() setter
print(f"New salary: ${emp.salary}")

emp.salary = -100                    # Invalid

# Read-only property
print(f"Annual salary: ${emp.annual_salary}")

# Cannot set read-only property
# emp.annual_salary = 100000  # ✗ AttributeError!

# ============================================================================
# WHY ENCAPSULATION?
# ============================================================================
print("\n" + "="*60)
print("WHY USE ENCAPSULATION?")
print("="*60)

# Without encapsulation
class BadAccount:
    def __init__(self):
        self.balance = 0  # Public - anyone can modify!

bad_acc = BadAccount()
bad_acc.balance = 1000000  # Oops! Directly set to million
print(f"Bad account balance: ${bad_acc.balance}")

# With encapsulation
class GoodAccount:
    def __init__(self):
        self.__balance = 0  # Private
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

good_acc = GoodAccount()
# good_acc.__balance = 1000000  # ✗ Cannot access!
good_acc.deposit(1000)  # ✓ Must use method
print(f"Good account balance: ${good_acc.get_balance()}")

benefits = """
BENEFITS OF ENCAPSULATION:

1. DATA PROTECTION
   - Prevent direct modification
   - Validate before changing

2. FLEXIBILITY
   - Change internal implementation
   - External code remains same

3. MAINTENANCE
   - Easier to debug
   - Controlled access points

4. ABSTRACTION
   - Hide complex details
   - Simple interface for users
"""
print(benefits)

# ============================================================================
# PRACTICAL EXAMPLE: User Authentication
# ============================================================================
print("\n" + "="*60)
print("PRACTICAL EXAMPLE: User Authentication")
print("="*60)

class User:
    """User with encapsulated password"""
    
    def __init__(self, username, password):
        self.username = username      # Public
        self.__password = None        # Private
        self.set_password(password)   # Use setter for validation
    
    def set_password(self, password):
        """Set password with validation"""
        if len(password) >= 8:
            # In real app, would hash the password
            self.__password = f"hashed_{password}"
            print(f"Password set for {self.username}")
        else:
            print("Password must be at least 8 characters")
    
    def verify_password(self, password):
        """Verify password"""
        hashed = f"hashed_{password}"
        return self.__password == hashed
    
    def change_password(self, old_password, new_password):
        """Change password"""
        if self.verify_password(old_password):
            self.set_password(new_password)
            print("Password changed successfully")
        else:
            print("Incorrect old password")

# Create user
print("\n--- User Account ---")
user = User("alice", "secure123")

# Cannot access password directly
# print(user.__password)  # ✗ Error!

# Verify password
print("\n--- Verification ---")
print(f"Correct password: {user.verify_password('secure123')}")
print(f"Wrong password: {user.verify_password('wrong')}")

# Change password
print("\n--- Password Change ---")
user.change_password("wrong", "newpass123")     # Fails
user.change_password("secure123", "newpass123") # Success

# ============================================================================
# ENCAPSULATION IN TEST AUTOMATION
# ============================================================================
print("\n" + "="*60)
print("ENCAPSULATION IN TEST AUTOMATION")
print("="*60)

class LoginPage:
    """Page Object with encapsulated locators"""
    
    def __init__(self, driver):
        self.__driver = driver
        # Private locators - users don't need to know
        self.__username_field = ("id", "username")
        self.__password_field = ("id", "password")
        self.__submit_button = ("id", "submit")
    
    # Public interface
    def login(self, username, password):
        """Public method - simple interface"""
        print(f"Logging in as {username}")
        self.__enter_username(username)
        self.__enter_password(password)
        self.__click_submit()
    
    # Private helper methods
    def __enter_username(self, username):
        """Private - internal implementation"""
        print(f"  Entering username in {self.__username_field}")
    
    def __enter_password(self, password):
        """Private - internal implementation"""
        print(f"  Entering password in {self.__password_field}")
    
    def __click_submit(self):
        """Private - internal implementation"""
        print(f"  Clicking {self.__submit_button}")

# Usage
print("\n--- Using LoginPage ---")
driver = "MockDriver"
page = LoginPage(driver)

# Simple public interface
page.login("testuser", "password123")

# Cannot access private locators
# print(page.__username_field)  # ✗ Error!

print("""
BENEFITS:
✓ Locators are hidden from test code
✓ Can change locators without breaking tests
✓ Simple, clean test interface
✓ Implementation details encapsulated
""")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
ENCAPSULATION:
✓ Bundle data + methods together
✓ Restrict direct access to data
✓ Protect sensitive information

ACCESS MODIFIERS:
✓ Public (var): Accessible anywhere
✓ Protected (_var): Convention for internal use
✓ Private (__var): Name mangling, restricted access

BEST PRACTICES:
✓ Use private variables for sensitive data
✓ Provide public methods (getters/setters)
✓ Validate in setters
✓ Use @property for Pythonic access

WHY ENCAPSULATION?
✓ Data protection
✓ Validation
✓ Flexibility to change implementation
✓ Easier maintenance
✓ Hide complexity

GETTERS/SETTERS:
✓ Regular methods: get_x(), set_x()
✓ @property: Pythonic way (recommended)
✓ Can add validation logic
✓ Can make read-only properties

INTERVIEW ANSWER:
"Encapsulation bundles data and methods while restricting 
direct access. I use private variables (__var) with public 
methods to protect data and add validation. In my framework, 
page objects encapsulate locators, exposing only action methods."

PRACTICAL USES:
✓ Bank accounts (protect balance)
✓ User authentication (hide password)
✓ Page objects (hide locators)
✓ Configuration management (validate settings)
"""

print("\n" + "="*60)
print("✓ Encapsulation mastered!")
print("="*60)