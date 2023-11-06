# A importância de R$780.000 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:
# - o primeiro ganhador receberá 46%;
# - o segundo receberá 32%;
# o terceiro receberá o restante;
# Calcule e imprima a quantia ganha por cada um dos ganhadores.

g1 = (780000 * 0.46)
g2 = (780000 * 0.32)
g3 = g1 - g2

print(f'O primeiro ganhador recebeu R${g1}, o segundo, R${g2} e o terceiro R${g3:.2f}.')