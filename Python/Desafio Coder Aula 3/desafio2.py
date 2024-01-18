frase = input('digite uma frase:')

string = frase.split()

for letra in string:
    tamanho = len(letra)
    print (letra, tamanho)