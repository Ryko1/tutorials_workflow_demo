from django.test import TestCase
from django.urls import reverse
import pytest

# Create your tests here.
# Integration Test: User Login
@pytest.fixture
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username='test_username', password='test_password'
    )
    return "test_username", "test_password" #--returns a tuple

def test_login_user(client, test_user):
    test_username, test_password = test_user    #--unpacks the tuple
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True
