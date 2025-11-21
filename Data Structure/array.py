

import array 

arr1 = array.array('i',[10,20,30,40,50])

print(arr1)

s1 = b'abcdef'

arr2 = array.array('b',s1)

print(arr2)

print(arr2[2])

print(arr2[1:3])

arr2.append(103)

print(arr2)

print(arr2.index(101))

print(arr2.typecode)