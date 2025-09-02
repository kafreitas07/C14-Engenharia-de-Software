import numpy as np 
from main import matriz_b

matriz_b_np = np.array(matriz_b)

def test_matriz_b_number():
    assert np.issubdtype(matriz_b_np.dtype, np.number)
    

#testa se a matriz b possui apenas números
