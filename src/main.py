import numpy as np

matriz_a = np.arange(1,10,1).reshape(3,3)
matriz_b = np.arange(1,10,1).reshape(3,3)

def calcular_matriz():
   return np.mean(matriz_a, matriz_b)

if __name__ == '__main__':
    resultado =calcular_matriz()
    print (resultado)

