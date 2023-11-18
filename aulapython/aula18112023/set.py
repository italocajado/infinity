lista = [1,2,6,9,5,2]
set = set(lista)
print(type(set))

set.pop()
print('lista com um elemento removido: ', set)


if 9 in set:
    print(set)
else:
    print('não temos o numero 9 no conjunto')

set.add(10)
print(set)

set.remove(5)
print(set)

setCo = set.copy()
print(setCo)

set2 = {80, 90, 42}
set2.update(set)
print(set2)

set3 = setCo.union(set2)
print(set3)