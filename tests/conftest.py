import pytest
from fastapi.testclient import TestClient

from config import Settings
from main import app


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope='session')
def test_settings():
    return Settings()
