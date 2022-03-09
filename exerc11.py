# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
vetor2 = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
vetor3 = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
vetor4 = []
for i in range(10):
    vetor4.append(vetor1[i])
    vetor4.append(vetor2[i])
    vetor4.append(vetor3[i])
print(vetor4)
