# Sejam  a e b catetos de um triângulo, onde a hipotenusa é obtida pela equação:
# h = raiz quadrada de a² + b².
# Faça um progrma que receba os valores de a e b e calcule po valorda hipotenusa através da equação.

from math import sqrt

a = int(input('a: '))

b = int(input('b: '))

h = sqrt(a ** 2 + b ** 2)

print(f'O valor da hipotenusa é {h:.2f}')

