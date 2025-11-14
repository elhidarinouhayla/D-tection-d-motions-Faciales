import tensorflow as tf
import pytest
import sys
import os
from fastapi.testclient import TestClient
import numpy as np


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import app
from database import Base,engine
from DL.detect_and_predict import emotion_detection
@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
# Vérification du sauvegarde du modele 
@pytest.fixture
def model():
    return tf.keras.models.load_model("DL/emotion_cnn_model.keras")

def test_model_loads(model):
    assert model is not None


# Vérification du format de la prédiction
@pytest.fixture
def client():
    return TestClient(app)


def test_format_predection(client):
    request = client.get("/predictions")
    assert request.status_code == 200

    data = request.json()
    assert isinstance(data, list)

    if data:
        dict = data[0]
        for key in ["id", "emotion", "confidence", "created_at"]:
            assert key in dict


    