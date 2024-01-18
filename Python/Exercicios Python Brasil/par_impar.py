numeros = [5,10,85,77,23,36,45,6,2,66,99,81,42,37,4,13,22,29,51,70]
par = []
impar = []
for numero in numeros:
    if (numero % 2) == 0:
        par.append(numero)
    else:impar.append(numero)
print(numeros, par, impar)
