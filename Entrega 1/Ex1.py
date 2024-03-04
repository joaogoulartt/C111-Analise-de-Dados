mundial_clubes = [
    "Real Madrid",
    "Bayern de Munique",
    "Milan",
    "Barcelona",
    "São Paulo",
]

print('Os 5 maiores campeões do Mundial de Clubes da FIFA são:')
print(mundial_clubes)
print('')
print('Os 3 primeiros colocados são:')
print(mundial_clubes[:3])
print('')
print('Os 2 últimos colocados são:')
print(mundial_clubes[-2:])
print('')
print('Colocando em ordem alfabética:')
print(sorted(mundial_clubes))
print('')
print('O Barcelona está na posição:')
print(mundial_clubes.index('Barcelona') + 1)