import numpy as np
from main import calcular_matriz

def test_soma_matrizes_com_tipos_diferentes():
    matriz_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=int)
    matriz_b = np.array([["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]], dtype=str)  
    
    try:
        resultado = calcular_matriz()
    except ValueError:
        pass  
    else:
        assert False, "Esperado erro devido à soma de matrizes com tipos de dados diferentes!"


#teste onde verifica se as matrizes não são do mesmo tipo