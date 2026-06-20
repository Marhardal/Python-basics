sets = {1, 2, 3, 4, 5}

print(type(sets))

sets.add(6)

print(sets)

sets.remove(2)

print(sets)

print(3 in sets)

print(2 in sets)

sets2 = {4, 5, 6, 7, 8}

print(sets.union(sets2))

print(sets.intersection(sets2))

print(sets.difference(sets2))

print(sets.symmetric_difference(sets2))

print(sets.issubset(sets2))

print(sets.issuperset(sets2))

print(sets.isdisjoint(sets2))

