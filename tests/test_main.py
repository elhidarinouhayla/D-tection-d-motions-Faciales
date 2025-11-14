import tensorflow as tf
import pytest
import sys
import os
from fastapi.testclient import TestClient
import numpy as np

# Permet d'importer main.py dans tests/
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

@pytest.fixture
def model():
    return tf.keras.models.load_model("DL/emotion_cnn_model.keras")

def test_model_loads(model):
    assert model is not None


@pytest.fixture
def client():
    return TestClient(app)


def test_format_predection(client):
    response = client.get("/predictions")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

    if data:
        first = data[0]
        for key in ["id", "emotion", "confidence", "created_at"]:
            assert key in first
