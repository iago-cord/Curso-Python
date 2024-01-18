import numpy as np
import pandas as pd

array_inteiro = np.random.randint(1,100, size = 10)

print(array_inteiro)

matriz = np.random.rand(5,5)

print('Minimo', matriz.min())
print('Maximo', matriz.max())
print('Media', matriz.mean())

array10 = np.random.rand(10)

arraymult = array10 * 10

print(arraymult.astype(int))

array2 = np.random.randint(0,9, size = (2,3,3))

array2[1,:]  = -1

print(array2)


df = pd.DataFrame({
    'Fruta': ['Banana', 'Maca', 'Pera'],
    'Preço': [ 7.90,10.20,11.80],
    'Quantidade': [12,3,4]
})

print(df)