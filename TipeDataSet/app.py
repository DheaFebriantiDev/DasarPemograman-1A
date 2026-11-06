setA = {'apel', 'jeruk', 'durian', 8}

for item in setA:
    print(item)

setA.add('semangka')
setB = {'makanan', 'melon'}
setA.update(setB)
setB.intersection_update(setA)
print(setA)
print(setB)
setA.symmetric_difference_update(setB)
setA.pop()