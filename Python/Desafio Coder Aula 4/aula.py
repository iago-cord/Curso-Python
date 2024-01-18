def mul(a,b):   
    x = a*b
    return x

print(mul(4,5))

def imc(peso,altura):
        imc = peso/altura**2
        return imc
print(imc(68,1.78))


x=200
print('a',x)
def mostrax(x):
    print('c',x)
    x = 3
    print('d',x)
print ('b',x)
mostrax(10)
print('e',x)

def calcular_imposto(salario, taxa = 0.1):
     imposto  = salario * taxa
     print('imposto de:',imposto)

calcular_imposto(5000,0.15)
calcular_imposto(5000,0.1)
calcular_imposto(5000)
#calcular_imposto(int(input('Digite o seu salario:')),0.2)

quadrado = lambda x: x ** 2
print(quadrado(4))

e_par = lambda x: (x%2) == 0
print(e_par(9))

frutas = ['banana', 'pera','tomate']
tamanhos = map(len,frutas)
print(list(tamanhos))

lista_quadrados = list(map(quadrado, [3,4,5]))
print(lista_quadrados)

from datetime import date

print(date.today())