import numpy as np 
from main import matriz_b

def test_matriz_b_forma_3x3():
    assert isinstance(matriz_b, np.ndarray)
    assert matriz_b.shape == (3, 3)


    #teste se a matriz B é uma matriz 3x3