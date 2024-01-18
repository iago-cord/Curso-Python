def primeiro_nome(nome):
    
    for nome in nomes:
        primeiro = nome.strip()

    return primeiro

nomes = ['Joao Carlos','Maria Eduarda','Ana Rute', 'Ana Clara']

print(primeiro_nome(nomes))