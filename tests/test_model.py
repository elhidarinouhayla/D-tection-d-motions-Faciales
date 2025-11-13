import tensorfow as tf
import pytest


@pytest.fixture
def model():
    return tf.keras.models.load_model("DL/emotion_cnn_model.keras")

def test_model_loads(model):
    assert model is not None