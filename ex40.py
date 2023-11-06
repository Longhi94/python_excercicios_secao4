# Uma empresa contrata um encanador a R$30,00 por dia. Faça um progrma que solicite o número de dias trabalhados pelo encanador e impirma a quantidade liquida
# que deveráser paga, sabendo-se que são descontados 8% para imposto de renda.

dias_trabalhados = int(input('dias trabalhados: '))

pagamento = dias_trabalhados * 30

r = pagamento - (pagamento * 0.08)

print(f'O encandor receberá R${r}.')