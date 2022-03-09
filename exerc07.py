# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
import random
import numpy

numeros = []
produto = 1
for i in range(5):
    numero = random.randint(1, 100)
    numeros.append(numero)

print(f"A soma do vetor é: {sum(numeros)}")
print(f"A multiplicação do vetor é: {numpy.prod(numeros)}")
print(f"O vetor é : {numeros}")
