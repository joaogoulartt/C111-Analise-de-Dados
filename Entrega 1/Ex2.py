loja_a = {
    "Mi 11 Lite",
    "Mi 11 Lite 5G",
    "Iphone 12",
    "Motorola G9 Plus",
    "Motorola G9 Play",
}

loja_b = {
    "Mi 11 Lite",
    "Iphone 12",
    "Samsung Galaxy A52",
    "Samsung Galaxy A72",
    "Poco X3 Pro",
}

print('Os produtos em comum entre as lojas são:')
print(loja_a.intersection(loja_b))
print('')
print('Todos os produtos das duas lojas são:')
print(loja_a.union(loja_b))