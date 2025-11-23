import pytest  # type: ignore
from fastapi.testclient import TestClient


def test_sample_pass(client: TestClient):
    response = client.get("/home")
    print(response.status_code)
    assert False
