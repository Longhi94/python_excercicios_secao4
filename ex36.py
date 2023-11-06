# Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume circular de um cilindro  circular é calculado com a seguinte formula:
# v = 3.14 * raio² * altura

altura = int(input('altura: '))
raio = int(input('raio: '))

v = 3.14 * (raio ** 2) * altura

print(f'O volume do cilindro é {v}.')