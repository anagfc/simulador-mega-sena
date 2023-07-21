from random import randint
from time import sleep

aposta = []
sorteio = []
acertos = []
resultado = 0
numero = 0

titulos = ['simulador de mega sena', 'resultado']

while len(sorteio) < 6:
    sorteio.append(randint(1,60))
sorteio = set(sorted(sorteio, reverse=False))

print(f'\n{titulos[0]:^34}'.upper())
print('- $ ' * 9, '\n')

while len(aposta) < 6:
    numero = int(input('Insira um número para apostar: '))
    if numero <= 0 or numero > 60:
        print('Aposta inválida. Insira um número ente 1 e 60.\n')
    elif numero in aposta:
        print('Aposta repetida. Escolha um novo número.\n')
    else:
        aposta.append(numero)
aposta = set(sorted(aposta, reverse=False))

sleep(0.5)
print('\nRegistrando sua aposta...\n')
sleep(1)
print('\n', '- $ ' * 9)

acertos = set(aposta.intersection(sorteio))
resultado = len(acertos)

print(f'\n{titulos[1]:^34}'.upper(), '\n')
print(f'Sua aposta: {aposta}')
print('-' * 36)
print(f'Sorteados: {sorteio}')
print('-' * 36)
print(f'Você acertou {resultado} números: {acertos}\n' if resultado != 0 else f'Você acertou {resultado} números.\n')
print('- $ ' * 9, '\n')
