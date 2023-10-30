#Leia uma temperatura em kelvin e apresente-a convertida em celsius.
# formula: c = k - 273.15

k = float(input('kelvin: '))

c = k - 273.15

print(f'{c:.2f}°C')