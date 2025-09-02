import numpy as np
from main import matriz_b

def test_matriz_apenas_positivos():
    assert np.all(matriz_b > 0)




#testa se a matriz B possui apenas números inteiros