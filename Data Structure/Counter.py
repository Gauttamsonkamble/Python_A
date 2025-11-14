
from collections import Counter

L = ['mark','jonny','David','mark','jonny','mark','james','mathew']

c = Counter(L)

print(c)

print(c['mark'])

print(c.get('mark'))

print(c.keys())

print(c.values())

c.update({"Ajay":4})

print(c)

for i in c.elements():
    print(i)

c.pop('Ajay')

print(c)

print(c.most_common(1))
print(c.most_common(2))

c.update({'Ajay':4})

print(c.most_common(2))