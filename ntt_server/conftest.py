import os
import sys
from fastapi.testclient import TestClient
from server import app
import pytest


def pytest_configure():
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c
