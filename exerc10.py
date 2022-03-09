# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores
# deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
vetor2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
vetor3 = []
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print(vetor3)
