# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos
# possuem altura inferior à média de altura desses alunos.

import random

lista_idade = []
lista_altura = []
mais_13anos = 0
altura_menor_media = 0
for i in range(30):
    idade = random.randint(0, 100)
    altura = random.randint(50, 200)
    lista_idade.append(idade)
    lista_altura.append(altura)

soma = sum(lista_altura)
media = soma / len(lista_altura)

for i in range(30):
    if lista_idade[i] > 13:
        mais_13anos += 1
    if lista_altura[i] < media:
        altura_menor_media += 1


print(f"A lista de idade dos alunos é: {lista_idade}")
print(f"A lista de altura dos alunos é: {lista_altura}")
print(f"A média de altura dos alunos é: {round(media,2)}cm.")
print(f"{mais_13anos} possuem mais que 13 anos.")
print(f"{altura_menor_media} possuem altura menor que a média.")


