def fatorial(numero = (int(input('Insira um numero:',))),contador = 1, resultado = 1):
    while contador <= numero:
        resultado *= contador
        contador + 1
    return resultado
    
print(fatorial())
