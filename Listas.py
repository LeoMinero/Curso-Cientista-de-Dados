# Formas de criar listas
lst = [1, 2, 3, 4, 5]
print(lst)

# Vários tipos
lst2 = [1, 2, 3, '4', True]
print(lst2)

# Lista com lista
lst3 = [12, [1, 2, 3, 4, 5], 'a']
print(lst3)

# Criando uma lista com range
lst4 = list(range(0,10))
print(lst4)

# Comprimento da lista
print(len(lst))

# Acessando elemento
print(lst[0])
# Posição 1 é uma lista
print(lst3[1])
# Alterando a posição
lst[0] = 4

# Percorrendo lista
for n in range(0, len(lst4)):
    print(lst4[n]+1)

