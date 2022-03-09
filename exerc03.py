# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
import random


lista_notas = []

for i in range(4):
    nota = random.uniform(0,10)
    lista_notas.append(round(nota,2))
soma = sum(lista_notas)
media = soma/len(lista_notas)
print(f"As notas foram: {lista_notas}")
print(f"A médias das notas foi {round(media,2)}")