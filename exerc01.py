# Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
import random

numeros = []

for _ in range(5):
    numero = random.randint(-100,100)
    numeros.append(numero)
print(numeros)