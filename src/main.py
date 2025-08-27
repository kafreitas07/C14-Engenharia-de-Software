import numpy as np

def calcular_matriz():
    matriz_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matriz_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    resultado = np.add(matriz_a, matriz_b)

    return resultado

if __name__ == '__main__':
    resultado =calcular_matriz()
    print (resultado)
