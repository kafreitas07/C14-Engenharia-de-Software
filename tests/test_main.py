import numpy as np
from main import calcular_matriz  # mantenha só este import

def test_calcular_matriz():
    resultado_esperado = np.array([[10, 10, 10],
                                   [10, 10, 10],
                                   [10, 10, 10]])
    resultado_obtido = calcular_matriz()
    # mensagens de erro melhores que array_equal
    np.testing.assert_array_equal(resultado_obtido, resultado_esperado)


#Criei o teste baseado em um só resultado, alterei um pouco a minha função para que ela retorne somente um valor, no caso todos serão 10 para esse teste
# no caso do pytest, pelo que vi, ele só funciona se inserirmos o nome "test" no nome da função, para que ele interprete que aquilo é um teste
