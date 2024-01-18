frutas = ["maçã","banana", "pera", "uva", "abacaxi"]
nova_fruta = input("Digite o nome de uma Fruta:")
for fruta in frutas:
    if fruta != nova_fruta:
        frutas.append(nova_fruta)
    break
    
print(frutas)
