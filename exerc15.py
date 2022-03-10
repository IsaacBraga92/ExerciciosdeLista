"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados
quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
    A- Mostre a quantidade de valores que foram lidos;
    B- Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    C- Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    D- Calcule e mostre a soma dos valores;
    E- Calcule e mostre a média dos valores;
    F- Calcule e mostre a quantidade de valores acima da média calculada;
    G- Calcule e mostre a quantidade de valores abaixo de sete;
    H- Encerre o programa com uma mensagem;
"""

notas = []
nota = 0
quantidade_notas_inseridas = soma = media = quantidade_acima_media = quantidade_abaixo_de_7 = 0
print("Para sair digite -1.")
while True:

    if nota == -1:
        break
    nota = float(input("Digite a nota: "))
    if nota != -1:
        notas.append(nota)
        quantidade_notas_inseridas += 1
soma = sum(notas)
media = soma/len(notas)
for i in notas:
    if i > media:
        quantidade_acima_media += 1
for i in notas:
    if i < 7:
        quantidade_abaixo_de_7 += 1
# A
print(f"A quantidade de notas inseridas é: {quantidade_notas_inseridas}")
# B
print(' '.join([str(nota) for nota in notas]))
# C
notas.reverse()
print('\n'.join([str(nota) for nota in notas]))
# D
print(f"A soma das notas é: {soma}")
# E
print(f"A média das notas é: {round(media,2)}")
# F
print(f"A quantidade de notas acima da média é: {quantidade_acima_media}")
# G
print(f"A quantidade de notas abaixo de 7 é: {quantidade_abaixo_de_7}")
# H
print("Fim do programa!")
