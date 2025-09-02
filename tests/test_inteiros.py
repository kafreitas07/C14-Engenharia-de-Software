import numpy as np
from main import matriz_a

def test_inteiros():
    assert np.issubdtype(matriz_a.dtype,int)
