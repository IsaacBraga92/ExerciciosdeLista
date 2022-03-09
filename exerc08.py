# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida
import random

lista_idade = []
lista_altura = []

for i in range(5):
    idade = random.randint(0,100)
    altura = random.randint(50,200)
    lista_idade.append(idade)
    lista_altura.append(altura)

print(f"A lista idade é: {lista_idade}")
print(f"A lista altura é: {lista_altura}")
lista_altura.reverse()
lista_idade.reverse()
print(f"A lista idade invertida é: {lista_idade}")
print(f"A lista altura invertida é: {lista_altura}")