# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

import random

numeros = []

for _ in range(10):
    numero = random.uniform(1,10)
    numeros.append(round(numero,2))
print(numeros)
numeros.reverse()
print(numeros)