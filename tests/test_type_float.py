import numpy as np
from main import calcular_matriz

def test_soma_matrizes_com_tipos_diferentes():
    matriz_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=int)
    matriz_b = np.array([[1.5, 2.5, 3.5], [4.5, 5.5, 6.5], [7.5, 8.5, 9.5]], dtype=float)
    
    try:
        resultado = calcular_matriz()
    except ValueError:
        pass  
    else:
        assert False

#verifica se possui inteiros juntos com float