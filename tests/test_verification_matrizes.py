import numpy as np
from main import matriz_a, matriz_b, calcular_matriz

def test_soma_nao_modifica_matrizes():
    matriz_a_original = matriz_a.copy()
    matriz_b_original = matriz_b.copy()
    
    calcular_matriz()
    
    assert np.array_equal(matriz_a, matriz_a_original), "matriz_a foi modificada!"
    assert np.array_equal(matriz_b, matriz_b_original), "matriz_b foi modificada!"


#verifica se as matrizes não foram modificadas na soma