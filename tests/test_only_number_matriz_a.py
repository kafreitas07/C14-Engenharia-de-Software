import numpy as np 
from main import matriz_a

matriz_a_np = np.array(matriz_a)

def test_matriz_a_number():
    assert np.issubdtype(matriz_a_np.dtype, np.number)
    
    #testa se a matriz A possui apenas números
