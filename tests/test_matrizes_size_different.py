import numpy as np
from main import calcular_matriz

def test_soma_matrizes_com_dimensoes_diferentes():
    matriz_a = np.random.randint(10**6, 10**8, size=(3, 3))
    matriz_b = np.random.randint(10**6, 10**8, size=(4, 3))  
    
    try:
        resultado = calcular_matriz()
    except ValueError:
        pass  
    else:
        assert False, "Esperado erro devido à soma de matrizes de dimensões diferentes!"


#teste onde calcula as matrizes de diferentes tamanhos, onde gera um teste com resultado falso