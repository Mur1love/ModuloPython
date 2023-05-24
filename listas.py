# Estrutura de Dados

notas = [6, 7, 8]

#Criando listas

lista = []
lista = list()
lista = [2, "Murilo", False]
listaDeListas = [3, [3,5,6], "Eu"]

#Indexacao e Slices

"""lista = [2, "Murilo", False]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[-1])""" #Ultimo elemento da lista


#Slices

"""lista = [1,2,3,4,5,6,7,8,9]
print(lista[0:6])
print(lista[2:])
print(lista[0:7:2])"""


#Iteracoes com FOR

nomes = ["Murilo",  'Bea', 'Lorenzo', 'Lara']

"""for i in nomes:
    print(i)"""


#Utilizando indices

"""print(len(nomes))

for i in range(len(nomes)):
    print(i) #Imprime os indices da lista

for i in range(len(nomes)):
    print(nomes[i]) #Imprime cada elemento da lista"""


# Metodos de Listas

mlista = [1,2,3,4]

#Append - Adiciona elementos na lista no final da lista

print(mlista)

mlista.append(5)

print('Insere um elemento aao final da lista: ', mlista)

#Insert - Adiciona o elementopor posicao 

mlista.insert(2,10)

print('Insere um elemento por posicao: ', mlista)

#Extend - juntar duas listas

nlista = [7,8,9,11]

mlista.extend(nlista)

print('Une duas listas: ', mlista)

#Pop - remove o ultimo elemento da lista

mlista.pop() #Um  indice da lista pode ser colocado para ser removido

print('Remove o ultimo elemento da lista: ', mlista)

#Remove - Remove o primeiro que tem o valor do elemento da lista

mlista.remove(10)

print('Remove o elemento 10 da lista: ', mlista)

#Count - quantidade de certo elemento na lista

print('Quantidade de 1ns na lista: ', mlista.count(1))


#Index - Mostra o indice de certo elemento da lista

print('Mostra o indice do elemento 7: ', mlista.index(7))

#Sort - ordena a lista

mlista.sort(reverse=True) #Ordena decrescente

print(mlista) 

#FUNCOES PARA LISTAS

# len - mostra o tamanho da lista

print(len(mlista))

# sum - retorna a soma dos elementos da lista

print('A soma dos elementos da lista:', sum(mlista))

# max - retorna o maior elemento da lista

print('O maior elemento da lista: ', max(mlista))

# min - retorna o menor elemento da lista

print('O menor elemento da lista: ', min(mlista))

