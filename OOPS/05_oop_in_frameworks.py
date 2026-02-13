"""
OOP in Test Automation Framework
==================================
Real-world application of OOP concepts in test automation
"""

from abc import ABC, abstractmethod

# ============================================================================
# OOP CONCEPTS IN SELENIUM FRAMEWORK
# ============================================================================
"""
How OOP concepts apply to test automation frameworks:

1. ENCAPSULATION - Hide locators and implementation
2. INHERITANCE - Reuse common page/test functionality
3. POLYMORPHISM - Different page validations
4. ABSTRACTION - Define test/page structure

Benefits:
- Maintainable code
- Reusable components
- Easy to extend
- Clean separation of concerns
"""

print("="*60)
print("OOP IN TEST AUTOMATION FRAMEWORK")
print("="*60)

# ============================================================================
# 1. ENCAPSULATION IN PAGE OBJECTS
# ============================================================================
"""
Encapsulation in frameworks:
- Hide locators (private)
- Expose only action methods (public)
- Protect implementation details
"""

print("\n--- 1. ENCAPSULATION: Page Objects ---")

class LoginPage:
    """Login page with encapsulated locators"""
    
    def __init__(self, driver):
        self.__driver = driver
        
        # Private locators - hidden from tests
        self.__username_field = ("id", "username")
        self.__password_field = ("id", "password")
        self.__submit_button = ("id", "submit")
        self.__error_message = ("css", ".error-msg")
    
    # Public methods - test interface
    def login(self, username, password):
        """
        Public method to login
        Tests don't need to know about locators!
        """
        print(f"Logging in as {username}")
        self.__enter_username(username)
        self.__enter_password(password)
        self.__click_submit()
    
    def get_error_message(self):
        """Public method to get error"""
        return self.__get_element_text(self.__error_message)
    
    # Private helper methods - implementation details
    def __enter_username(self, username):
        """Private: Enter username"""
        print(f"  Entering username: {self.__username_field}")
        # self.__driver.find_element(*self.__username_field).send_keys(username)
    
    def __enter_password(self, password):
        """Private: Enter password"""
        print(f"  Entering password: {self.__password_field}")
        # self.__driver.find_element(*self.__password_field).send_keys(password)
    
    def __click_submit(self):
        """Private: Click submit"""
        print(f"  Clicking submit: {self.__submit_button}")
        # self.__driver.find_element(*self.__submit_button).click()
    
    def __get_element_text(self, locator):
        """Private: Get element text"""
        # return self.__driver.find_element(*locator).text
        return "Error message"

# Usage in test
print("\nTest using LoginPage:")
driver = "MockDriver"
login_page = LoginPage(driver)

# Clean, simple interface!
login_page.login("testuser", "password123")
# Cannot access private locators
# print(login_page.__username_field)  # ✗ Error!

print("""
BENEFITS:
✓ Locators hidden from test code
✓ Can change locators without breaking tests
✓ Clean test code
✓ Implementation details encapsulated
""")

# ============================================================================
# 2. INHERITANCE IN FRAMEWORK
# ============================================================================
"""
Inheritance in frameworks:
- BasePage with common actions
- All pages inherit from BasePage
- Reuse click, wait, getText methods
"""

print("\n--- 2. INHERITANCE: Base Page ---")

class BasePage:
    """Base page with common methods"""
    
    def __init__(self, driver):
        self.driver = driver
    
    # Common methods all pages can use
    def click(self, locator):
        """Common click method"""
        print(f"BasePage: Clicking {locator}")
        # self.driver.find_element(*locator).click()
    
    def enter_text(self, locator, text):
        """Common text entry"""
        print(f"BasePage: Entering '{text}' in {locator}")
        # self.driver.find_element(*locator).send_keys(text)
    
    def get_text(self, locator):
        """Common get text"""
        print(f"BasePage: Getting text from {locator}")
        # return self.driver.find_element(*locator).text
        return "Sample text"
    
    def wait_for_element(self, locator, timeout=10):
        """Common wait"""
        print(f"BasePage: Waiting for {locator}")
        # WebDriverWait(self.driver, timeout).until(
        #     EC.presence_of_element_located(locator)
        # )

# Child pages inherit from BasePage
class InheritedLoginPage(BasePage):
    """Login page inherits common methods"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = ("id", "username")
        self.password_field = ("id", "password")
        self.submit_button = ("id", "submit")
    
    def login(self, username, password):
        """Use inherited methods"""
        self.enter_text(self.username_field, username)  # From BasePage!
        self.enter_text(self.password_field, password)  # From BasePage!
        self.click(self.submit_button)                   # From BasePage!

class DashboardPage(BasePage):
    """Dashboard page also inherits"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.welcome_msg = ("id", "welcome")
        self.logout_btn = ("id", "logout")
    
    def get_welcome_message(self):
        """Use inherited method"""
        return self.get_text(self.welcome_msg)  # From BasePage!
    
    def logout(self):
        """Use inherited method"""
        self.click(self.logout_btn)  # From BasePage!

# Usage
print("\nUsing inherited pages:")
driver = "MockDriver"

login = InheritedLoginPage(driver)
login.login("user", "pass")  # Uses inherited methods!

dashboard = DashboardPage(driver)
msg = dashboard.get_welcome_message()  # Uses inherited methods!
print(f"Welcome message: {msg}")

print("""
BENEFITS:
✓ No code duplication
✓ All pages have same base methods
✓ Easy to add new common functionality
✓ Consistent behavior across pages
""")

# ============================================================================
# 3. POLYMORPHISM IN FRAMEWORK
# ============================================================================
"""
Polymorphism in frameworks:
- Same method name (e.g., verify_page)
- Different implementation for each page
- Method overriding
"""

print("\n--- 3. POLYMORPHISM: Different Validations ---")

class PolymorphicBasePage(ABC):
    """Base page with abstract verify method"""
    
    def __init__(self, driver):
        self.driver = driver
    
    # Abstract method - each page implements differently
    @abstractmethod
    def verify_page(self):
        """Each page verifies differently"""
        pass

class PolymorphicLoginPage(PolymorphicBasePage):
    """Login page verification"""
    
    def verify_page(self):
        """Verify login page"""
        print("LoginPage: Checking for login form")
        print("  ✓ Username field exists")
        print("  ✓ Password field exists")
        print("  ✓ Submit button exists")
        return True

class PolymorphicDashboardPage(PolymorphicBasePage):
    """Dashboard page verification"""
    
    def verify_page(self):
        """Verify dashboard page"""
        print("DashboardPage: Checking dashboard elements")
        print("  ✓ Welcome message exists")
        print("  ✓ Navigation menu exists")
        print("  ✓ User profile visible")
        return True

class ProfilePage(PolymorphicBasePage):
    """Profile page verification"""
    
    def verify_page(self):
        """Verify profile page"""
        print("ProfilePage: Checking profile elements")
        print("  ✓ User info displayed")
        print("  ✓ Edit button exists")
        return True

# Polymorphic function - works with any page!
def verify_and_proceed(page):
    """
    Same function works with different page types!
    This is polymorphism in action
    """
    print(f"\nVerifying {page.__class__.__name__}:")
    if page.verify_page():
        print("✓ Page verified, proceeding...")
    else:
        print("✗ Page verification failed!")

# Usage - same function, different behaviors!
print("\nPolymorphic verification:")
driver = "MockDriver"

pages = [
    PolymorphicLoginPage(driver),
    PolymorphicDashboardPage(driver),
    ProfilePage(driver)
]

for page in pages:
    verify_and_proceed(page)  # Same call, different behavior!

print("""
BENEFITS:
✓ Same interface for all pages
✓ Easy to add new pages
✓ Test code remains same
✓ Flexible and extensible
""")

# ============================================================================
# 4. ABSTRACTION IN FRAMEWORK
# ============================================================================
"""
Abstraction in frameworks:
- Abstract base test class
- Defines test lifecycle
- Child tests implement specific validation
"""

print("\n--- 4. ABSTRACTION: Test Structure ---")

class BaseTest(ABC):
    """Abstract base test defining test lifecycle"""
    
    def __init__(self):
        self.driver = None
    
    # Concrete methods - common implementation
    def setup_driver(self):
        """Setup WebDriver"""
        print("BaseTest: Setting up driver")
        self.driver = "MockDriver"
    
    def teardown_driver(self):
        """Teardown WebDriver"""
        print("BaseTest: Tearing down driver")
        self.driver = None
    
    # Template method - defines structure
    def run_test(self):
        """Template method - test lifecycle"""
        print("\n" + "="*50)
        print(f"Running: {self.__class__.__name__}")
        print("="*50)
        
        self.setup_driver()
        self.setup_test()
        
        try:
            self.execute_test_steps()
            self.verify_test_results()
            print("✓ TEST PASSED")
        except AssertionError as e:
            print(f"✗ TEST FAILED: {e}")
        finally:
            self.teardown_test()
            self.teardown_driver()
    
    # Hook methods - child can override
    def setup_test(self):
        """Test-specific setup"""
        print("BaseTest: Default test setup")
    
    def teardown_test(self):
        """Test-specific teardown"""
        print("BaseTest: Default test teardown")
    
    # Abstract methods - child MUST implement
    @abstractmethod
    def execute_test_steps(self):
        """Execute test steps"""
        pass
    
    @abstractmethod
    def verify_test_results(self):
        """Verify results"""
        pass

# Concrete test implementations
class LoginTest(BaseTest):
    """Login test implementation"""
    
    def setup_test(self):
        """Login-specific setup"""
        print("LoginTest: Navigating to login page")
    
    def execute_test_steps(self):
        """Implement login steps"""
        print("LoginTest: Entering credentials")
        print("LoginTest: Clicking login button")
    
    def verify_test_results(self):
        """Verify login"""
        print("LoginTest: Verifying user logged in")
        print("LoginTest: Checking dashboard displayed")

class SearchTest(BaseTest):
    """Search test implementation"""
    
    def setup_test(self):
        """Search-specific setup"""
        print("SearchTest: Logging in first")
    
    def execute_test_steps(self):
        """Implement search steps"""
        print("SearchTest: Entering search query")
        print("SearchTest: Clicking search button")
    
    def verify_test_results(self):
        """Verify search"""
        print("SearchTest: Verifying results displayed")
        print("SearchTest: Checking result count")

# Run tests
login_test = LoginTest()
login_test.run_test()

search_test = SearchTest()
search_test.run_test()

print("""
BENEFITS:
✓ Consistent test structure
✓ Force implementation of key methods
✓ Easy to add new tests
✓ Template pattern for lifecycle
""")

# ============================================================================
# COMPLETE FRAMEWORK EXAMPLE
# ============================================================================
print("\n" + "="*60)
print("COMPLETE FRAMEWORK EXAMPLE")
print("="*60)

# Base classes combining all concepts
class FrameworkBasePage(ABC):
    """Complete base page with all OOP concepts"""
    
    def __init__(self, driver):
        self._driver = driver  # Protected
    
    # ENCAPSULATION: Common methods
    def _click(self, locator):
        """Protected helper"""
        print(f"Clicking: {locator}")
    
    def _enter_text(self, locator, text):
        """Protected helper"""
        print(f"Entering '{text}' in: {locator}")
    
    # ABSTRACTION: Must implement
    @abstractmethod
    def verify_page_loaded(self):
        pass

# INHERITANCE: Concrete pages
class CompleteLoginPage(FrameworkBasePage):
    """Login page using all OOP concepts"""
    
    def __init__(self, driver):
        super().__init__(driver)
        # ENCAPSULATION: Private locators
        self.__username = ("id", "user")
        self.__password = ("id", "pass")
        self.__submit = ("id", "submit")
    
    # Public interface
    def login(self, user, pwd):
        """ENCAPSULATION: Hide implementation"""
        self._enter_text(self.__username, user)
        self._enter_text(self.__password, pwd)
        self._click(self.__submit)
    
    # POLYMORPHISM: Override abstract method
    def verify_page_loaded(self):
        """Different verification per page"""
        print("Verifying login page loaded")

class CompleteDashboardPage(FrameworkBasePage):
    """Dashboard page using all OOP concepts"""
    
    def __init__(self, driver):
        super().__init__(driver)
        self.__logout = ("id", "logout")
    
    def logout(self):
        self._click(self.__logout)
    
    # POLYMORPHISM: Different implementation
    def verify_page_loaded(self):
        """Different verification per page"""
        print("Verifying dashboard loaded")

# Usage
print("\n--- Using Complete Framework ---")
driver = "MockDriver"

login = CompleteLoginPage(driver)
login.verify_page_loaded()  # Polymorphism
login.login("user", "pass")  # Encapsulation

dashboard = CompleteDashboardPage(driver)
dashboard.verify_page_loaded()  # Polymorphism
dashboard.logout()

# ============================================================================
# INTERVIEW ANSWER TEMPLATE
# ============================================================================
print("\n" + "="*60)
print("INTERVIEW ANSWER TEMPLATE")
print("="*60)

interview_answer = """
"In my test automation framework, I use all four OOP concepts:

1. ENCAPSULATION:
   - Page objects hide locators (private variables)
   - Only expose action methods (public interface)
   - Example: LoginPage.login() hides internal locator details
   - Benefits: Maintainable, locators can change without affecting tests

2. INHERITANCE:
   - BasePage with common methods (click, wait, getText)
   - All page objects inherit from BasePage
   - Example: LoginPage extends BasePage
   - Benefits: Code reuse, no duplication, consistent behavior

3. POLYMORPHISM:
   - Same method name, different implementations
   - Example: verify_page() method in each page class
   - Each page verifies differently but same interface
   - Benefits: Flexible, easy to extend, uniform test code

4. ABSTRACTION:
   - Abstract BaseTest class defines test structure
   - Child tests implement execute_test() and verify_results()
   - Example: LoginTest extends BaseTest
   - Benefits: Enforces structure, consistent test lifecycle

This makes the framework:
✓ Easy to maintain
✓ Scalable for new pages/tests
✓ Follows design patterns (Page Object Model)
✓ Clean separation of concerns"
"""
print(interview_answer)

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
OOP IN TEST AUTOMATION:

ENCAPSULATION:
✓ Hide locators in page objects
✓ Expose only action methods
✓ Private variables for implementation
✓ Public methods for test interface

INHERITANCE:
✓ BasePage for common functionality
✓ All pages extend BasePage
✓ Reuse click, wait, getText methods
✓ Don't repeat code

POLYMORPHISM:
✓ Same method name across pages
✓ Different implementation per page
✓ verify_page(), validate(), etc.
✓ Uniform interface for tests

ABSTRACTION:
✓ Abstract BaseTest for structure
✓ Define test lifecycle
✓ Force implementation of key methods
✓ Template pattern

BENEFITS:
✓ Maintainable code
✓ Scalable framework
✓ Easy to extend
✓ Follows best practices
✓ Clean test code

INTERVIEW FOCUS:
✓ Give concrete examples from your framework
✓ Explain WHY you used each concept
✓ Mention specific benefits
✓ Show understanding of design patterns
"""

print("\n" + "="*60)
print("✓ OOP in Test Automation mastered!")
print("="*60)