#Leia uma temperatura em graus celsius e apresente-a em graus fahrenheit.
# formula: f = c * (9/5) + 32

c = float(input('celsius: '))

f = c * (9/5) + 32

print(f'{f:.2f}°F')