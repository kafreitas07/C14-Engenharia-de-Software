import numpy as np
from main import matriz_a, matriz_b, calcular_matriz

def test_matrizes_sao_numpy_array():
    assert isinstance(matriz_a, np.ndarray), "matriz_a não é do tipo numpy.ndarray!"
    assert isinstance(matriz_b, np.ndarray), "matriz_b não é do tipo numpy.ndarray!"
    
    resultado = calcular_matriz()
    assert isinstance(resultado, np.ndarray), "O resultado da soma não é do tipo numpy.ndarray!"


#teste para verificar se a minha matriz é do tipo ndarray, onde garente a soma correta