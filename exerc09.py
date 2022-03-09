# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
import random
a = []
for i in range(10):
    numero = random.randint(1, 20)
    a.append(numero)
soma = 0
for c in a:
    soma += c**2
print(f"A soma dos elementos do vetor ao quadrado é: {soma}")
