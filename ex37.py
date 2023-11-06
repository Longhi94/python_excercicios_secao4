# Faça um programa que leia o valor de um prouto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%.

v = int(input('valor do produto: '))

d = v - (v * 0.12)

print(f'O valor do produto com desconto é {d:.2f}.')