# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
import random
from cmath import inf

numeros_inteiros = []
numeros_pares = []
numeros_impares = []
numero = 0
for i in range(20):
    numero = random.randint(0, 1000)
    numeros_inteiros.append(numero)
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print(
    f"Lista de números: {numeros_inteiros}\nLista números pares: {numeros_pares}\nLista números impares: {numeros_impares}")
