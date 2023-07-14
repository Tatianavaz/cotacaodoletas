#testes de variáveis
print ('estudos de python')
input('insira um valor:')

idade = 26
print(idade)

nome = 'tatiana'

print(nome)
####
idade = 27
altura = 1,63
nome = 'Tatiana'
estudando = True

print(type(nome))
print(type(idade))
print(type(altura))
print(type(estudando))
###
linguagem = input('Qual seu curso favorito?')
print('estou estudando:', linguagem)

### Operadores
numero1 = 10
numero2 = 20

print(numero1 + numero2)
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2)
print(numero1 // numero2)
print(20 % 3)
print(2 ** 3)

# Operadores booleanos

idade1 = 10
idade2 = 15
print(idade1 >= idade2)

#### conversoes de tipos
altura = float(input('informe sua altura:'))
print(altura, type(altura))


####### condicionais
a = 5
b = 3
soma = a + b

if soma == 8:
    print ('A soma é 8!')
else:
    print('a soma não é 8')
          
for n in range(5):
    print(n)
    

# a média dos alunos deve sermaior igua a 7, do contrário será reprovado

media = float(input('informe sua nota:'))

if media >=7:
    print('Aprovado')
elif media >=5:
    print('Recuperação')
else:
    print('reprovado')

# apresentando duas ou mais condições a serem cumpridas

media = 5
presença = 50

if media >=7 and presença >= 70:
    print('Aprovado')
else:
    print('Reprovado')

# utilizaçãpo do while

numero_sortesdo = 15

numero_escolhido = int(input('informe o numero entre 1 e 20:'))

while numero_escolhido != numero_sortesdo:
    print('Errou, tente de novo')
    numero_escolhido = int(input('informe o numero entre 1 e 20:'))
    print('Acertou!')

## contador, estrutura contrlada de repetição

contador = 0

while contador < 5:
    print(contador)

    contador = contador + 1