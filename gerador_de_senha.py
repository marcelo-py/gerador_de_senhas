from random import randint, choice, shuffle
"""gerador de senha simples
    ele basicamente pega todo tipo de caractere digitado pelo usuário
     e depois de cada um deles é colocado um número de 1 a 10 e mais um símbolo"""
letras = list()
senha = list()
chave = input('Digite a base da sua senha: ')
while len(chave) > 8:
    chave = input('A base só pode ter até 8 caracteres, digite a base da sua senha novamente: ')
for c in range(0, len(chave)):
    letras.append(chave[c])
    senha.append(letras[:])
    letras.pop()
caracteres = (')', '*', '/', '%', '!')
print('a senha gerada é: ')
shuffle(senha)
cores = ('\033[1;31m', '\033[1;32m', '\033[1;33m')
for i, l in enumerate(senha):
    adcionais = randint(0, 10)
    p = l[:][0]
    p += str(adcionais) + choice(caracteres)
    print(p,end='')
print('\n\033[32;1mBoa sorte em decorar ela!')
