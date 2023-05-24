#Dicionarios

#Criando Dicionarios

lista = {}
dicionario = dict()


dicionario = { 'nome': 'Murilo', 'idade': 20, 'altura': 1.77}

print(dicionario)
print(dicionario['idade'])


#Adicionar elementos a um dicionario

dicionario['programador'] = True
print(dicionario)

dicionario['altura'] = 1.80 #sobrescreve o valor em tal chave
print(dicionario)

#Iterando sobre um dicionario

for chave in dicionario:
    print(chave, dicionario[chave])

#Testando a existencia de uma chave
print('peso' in dicionario) #False
print('idade' in dicionario) #True
