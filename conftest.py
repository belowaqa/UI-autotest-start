import pytest

@pytest.fixture
def user_data():
    return {
        "email": "user@example.com",
        "username": "testuser",
        "password": "password123"
    }
