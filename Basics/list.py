list1 = [1, 2, 3, 4, 5]

print(type(list1))

print(list1[3])

print(3 in list1)

list1.append(6)

print(list1)

# list1.remove(2)
list1.pop(2)

print(list1)

list1.reverse()
print(list1)

list2 = [7, 8, 9]

list3 = list1 + list2

print(list3)

list3.sort()

print(list3)

list3.append(3)

print(list3)

print(list3.count(3))

print(list3.index(3))

print(list3[0:5])

print(list3[-5:])
