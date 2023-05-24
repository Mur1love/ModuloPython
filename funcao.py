# FUNCOES

#Criando FUNCOES

#Funcoes Iniciais

def saudacao():
    print('Ola, seja bem-vindo!')

saudacao()

#Funcao com parametros

def saudacao(nome, idade):
    print(f'Ola, seja bem-vindo {nome}!')
    print(f'Voce tem {idade} anos de idade!')

saudacao('Murilo', 20)

#Funcao com parametros default

def saudacao(nome, idade=21):
    print(f'Ola, seja bem-vindo {nome}!')
    print(f'Voce tem {idade} anos de idade!')

saudacao('Murilo')


#Funcoes com retono

def soma(n1, n2):
    return n1 + n2

res = soma(5, 7)

print(res)





