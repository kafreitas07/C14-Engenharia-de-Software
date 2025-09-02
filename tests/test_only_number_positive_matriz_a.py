import numpy as np
from main import matriz_a

def test_matriz_apenas_positivos():
    assert np.all(matriz_a > 0)
