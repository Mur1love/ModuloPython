# Estrutura de Dados

notas = [6, 7, 8]

#Criando listas

lista = []
lista = list()
lista = [2, "Murilo", False]
listaDeListas = [3, [3,5,6], "Eu"]

#Indexacao e Slices

lista = [2, "Murilo", False]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[-1]) #Ultimo elemento da lista


#Slices

lista = [1,2,3,4,5,6,7,8,9]
print(lista[0:6])
print(lista[2:])
print(lista[0:7:2])


#Iteracoes com FOR

nomes = ["Murilo",  'Bea', 'Lorenzo', 'Lara']

for i in nomes:
    print(i)


#Utilizando indices

print(len(nomes))

for i in range(len(nomes)):
    print(i) #Imprime os indices da lista

for i in range(len(nomes)):
    print(nomes[i]) #Imprime cada elemento da lista