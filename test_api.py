import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_register():
    """Test user registration"""
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "SecurePass123!",
        "password_confirm": "SecurePass123!"
    }
    response = requests.post(f"{BASE_URL}/auth/register/", json=data)
    print("Register:", response.status_code, response.json())
    return response.json().get('access_token')

def test_login():
    """Test user login"""
    data = {
        "email": "test@example.com",
        "password": "SecurePass123!"
    }
    response = requests.post(f"{BASE_URL}/auth/login/", json=data)
    print("Login:", response.status_code, response.json())
    return response.json().get('access_token')

def test_profile(token):
    """Test protected profile endpoint"""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/auth/profile/", headers=headers)
    print("Profile:", response.status_code, response.json())

def test_create_post(token):
    """Test creating a post"""
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "title": "My First Secure Post",
        "content": "This is the content of my first secure post created via API."
    }
    response = requests.post(f"{BASE_URL}/users/posts/", json=data, headers=headers)
    print("Create Post:", response.status_code, response.json())

if __name__ == "__main__":
    print("Testing Secure API...")
    token = test_register()
    if token:
        test_profile(token)
        test_create_post(token)