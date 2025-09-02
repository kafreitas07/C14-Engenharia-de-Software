import numpy as np 
from main import matriz_a

def test_matriz_a_forma_3x3():
    assert isinstance(matriz_a, np.ndarray)
    assert matriz_a.shape == (3, 3)
