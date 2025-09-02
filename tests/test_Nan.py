import numpy as np
from main import calcular_matriz

def test_soma_com_nan():
    matriz_a = np.array([[1, 2, np.nan], [4, 5, 6], [7, 8, 9]])
    matriz_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]]) 
    
    try:
        
        resultado = calcular_matriz()
    except ValueError:
        pass  
    else:
        assert False


#verifica se possui valores Nun nas matrizes