import pytest
import requests


def test_endpoint():
    endpoint = 'http://localhost:8000/api?slack_name=udochukwu&track=frontend'
    response = requests.get(endpoint)
   
    assert response.status_code == 200