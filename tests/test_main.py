import tensorflow as tf
import pytest
import sys
import os
from fastapi.testclient import TestClient
import numpy as np

# Permet d'importer main.py depuis tests/
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app

# 🔹 Skip le test du modèle si le fichier n'existe pas
MODEL_PATH = "DL/emotion_cnn_model.keras"

@pytest.fixture
def model():
    if not os.path.exists(MODEL_PATH):
        pytest.skip(f"Model file {MODEL_PATH} not found. Skipping test.")
    return tf.keras.models.load_model(MODEL_PATH)

def test_model_loads(model):
    assert model is not None


# 🔹 TestClient pour FastAPI
@pytest.fixture
def client():
    return TestClient(app)


def test_format_prediction(client):
    response = client.get("/predictions")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

    if data:
        first = data[0]
        # Remplace "create_at" par "created_at" si nécessaire
        expected_keys = ["id", "emotion", "confidence", "created_at"]
        for key in expected_keys:
            assert key in first
