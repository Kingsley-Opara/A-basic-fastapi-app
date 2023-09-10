import pytest
import requests


def test_endpoint():
    endpoint = 'https://an-api-service.onrender.com/api/?slack_name=udochukwu&track=frontend'
    response = requests.get(endpoint)
   
    assert response.status_code == 200