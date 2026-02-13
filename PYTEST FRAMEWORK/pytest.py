# How to pass test data to tests?

# Method 1: Pytest Parametrize


import pytest

@pytest.mark.parametrize("username, password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("admin", "admin123")
])
def test_login(username, password):
    # Test runs 3 times with different data
    login_page.login(username, password)

# Method 2: JSON File

# test_data.json
{
    "login": {
        "valid_user": {"username": "test", "password": "pass123"},
        "invalid_user": {"username": "wrong", "password": "wrong"}
    }
}

# Test file
import json

def load_test_data():
    with open("test_data.json") as f:
        return json.load(f)

def test_login():
    data = load_test_data()
    login_page.login(
        data["login"]["valid_user"]["username"],
        data["login"]["valid_user"]["password"]
    )

# Method 3: Excel (openpyxl)

import openpyxl

def get_excel_data(file, sheet):
    wb = openpyxl.load_workbook(file)
    ws = wb[sheet]
    
    data = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        data.append(row)
    return data

@pytest.mark.parametrize("username, password", get_excel_data("data.xlsx", "LoginData"))
def test_login(username, password):
    login_page.login(username, password)

# Method 4: Fixtures

# conftest.py
@pytest.fixture
def test_data():
    return {
        "username": "testuser",
        "password": "password123"
    }

# test file
def test_login(test_data):
    login_page.login(test_data["username"], test_data["password"])




