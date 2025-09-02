import numpy as np
from main import calcular_matriz  

def test_calcular_matriz():
    resultado_esperado = np.array([  [2, 4, 6],
                                     [8, 10, 12],
                                     [14, 16, 18]])
    resultado_obtido = calcular_matriz()
    np.testing.assert_array_equal(resultado_obtido, resultado_esperado)
