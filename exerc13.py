# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a
# média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . .)
import random

temp_media_mes = []
soma = 0
meses = ['1 - Janeiro', '2 - Fevereiro', '3 - Março', '4 - Abril', '5 - Maio', '6 - Junho', '7 - Julho', '8 - Agosto',
         '9 - Setembro', '10 - Outubro', '11 - Novembro', '12 - Dezembro']

for i in range(12):
    # print(i, end=' ')
    temperatura = random.uniform(0, 43)
    temp_media_mes.append(round(temperatura, 2))

media = sum(temp_media_mes)/len(temp_media_mes)
print(temp_media_mes)
print(f"A temperatura média foi de: {round(media,2)}")
c = 0
for i in temp_media_mes:
    if i > media:
        print(f"No mês {meses[c]} a temperatura {i} foi acima da média anual.")
    c += 1

