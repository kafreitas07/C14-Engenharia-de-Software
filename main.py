# main.py
import numpy as np

def calcular_matriz():
    # Criando duas matrizes 3x3
    matriz_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matriz_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    # Somando as duas matrizes
    resultado = np.add(matriz_a, matriz_b)

    print("Matriz A:\n", matriz_a)
    print("Matriz B:\n", matriz_b)
    print("Resultado da soma:\n", resultado)

if __name__ == '__main__':
    calcular_matriz()
