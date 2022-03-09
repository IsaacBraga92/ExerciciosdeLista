# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
import random
import string

letras = []
consoante = 0
vogais = ['a','e','i','o','u','A','E','I','O','U']
for i in range(10):
    letra = random.choice(string.ascii_letters)
    letras.append(letra)
    if letra not in vogais:
        consoante += 1

print(letras)
print(consoante)
