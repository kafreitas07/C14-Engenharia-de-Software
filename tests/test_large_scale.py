import numpy as np
from main import calcular_matriz
import time

def test_performance_matriz_grande():
    matriz_a = np.random.randint(10**6, 10**8, size=(1000, 1000))
    matriz_b = np.random.randint(10**6, 10**8, size=(1000, 1000))
    
    start_time = time.time()  
    
    resultado = calcular_matriz()
    
    end_time = time.time()  
    
    assert end_time - start_time < 1, "O tempo de execução foi muito longo para matrizes grandes!"
    
    assert resultado.shape == (1000, 1000), f"Esperado matriz de 1000x1000, mas obteve {resultado.shape}"


#verifica o desempenho da função com matrizes muito grandes
