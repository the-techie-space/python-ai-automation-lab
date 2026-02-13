# Fetch all links & check broken ones

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("https://example.com")

# Get all links
links = driver.find_elements(By.TAG_NAME, "a")

broken_links = []

for link in links:
    url = link.get_attribute("href")
    
    if url and url.startswith("http"):
        try:
            response = requests.head(url, timeout=5)
            if response.status_code >= 400:
                broken_links.append((url, response.status_code))
                print(f"BROKEN: {url} - {response.status_code}")
        except requests.exceptions.RequestException as e:
            broken_links.append((url, str(e)))
            print(f"ERROR: {url} - {e}")

print(f"\nTotal Links: {len(links)}")
print(f"Broken Links: {len(broken_links)}")

driver.quit()

# Write XPath expressions

# Basic XPath
driver.find_element(By.XPATH, "//input[@id='username']")

# Contains
driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")

# Starts-with
driver.find_element(By.XPATH, "//input[starts-with(@id, 'user')]")

# Multiple conditions (AND)
driver.find_element(By.XPATH, "//input[@type='text' and @name='email']")

# Multiple conditions (OR)
driver.find_element(By.XPATH, "//input[@type='text' or @type='email']")

# Parent traversal
driver.find_element(By.XPATH, "//input[@id='username']/parent::div")

# Following sibling
driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")

# Axes
driver.find_element(By.XPATH, "//table[@id='data']//tr[5]/td[3]")

# Dynamic XPath
driver.find_element(By.XPATH, f"//div[@data-test-id='{test_id}']")

