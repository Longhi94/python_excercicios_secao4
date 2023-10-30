# Leia uma temperatura emem graus fahrenheit e apresente-a convertida em celsius.
# formula: c = 5 * (f - 32) / 9

f = float(input('fahrenheit: '))

c = 5 * (f - 32) / 9

print(f'{c:.2f}°C')