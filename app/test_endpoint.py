import pytest
import requests


def test_endpoint():
    endpoint = 'https://an-api-service.onrender.com/api/?slack_name=udochukwu&track=frontend'
    response = requests.get(endpoint, timeout=60)
   
    assert response.status_code == 200
