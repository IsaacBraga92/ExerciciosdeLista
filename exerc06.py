# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.
import random

lista_media = []
contador = 0
for a in range(10):
    soma = 0
    for n in range(4):
        nota = random.uniform(5, 10)
        soma += round(nota, 2)
        media = soma / 4
    lista_media.append(round(media, 2))
    if lista_media[a] >= 7.0:
        contador += 1

print(lista_media)
print(contador)
