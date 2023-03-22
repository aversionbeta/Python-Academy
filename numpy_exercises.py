import numpy as np

lista = [1,2,3,4,5,6,7,8,9]
print(lista)

arr = np.array(lista)

type(arr)

print(arr)

matriz = [[1,2,3],[4,5,6],[7,8,9]]
matriz = np.array(matriz)

print(matriz)

#Indexing

print(arr[0]+arr[1])

print(matriz[0])

print(matriz[0,1])

#Slicing

print(arr[0:3])

print(arr[1:])

print(arr[0:2])

print(arr[:2])

print(arr[::3]) #Take everything and bring it counting 3 everytime

print(arr[:-2])

print(matriz[1:])

print(matriz[1:,0:2])

#Data Types

arrtype = np.array([1,2,3,4])

print(arrtype.dtype)

# arrtype = np.array([1,2,3,4], dtype='float64')

# print(arrtype.dtype)

arrtype = arrtype.astype(np.float64)

print(arrtype.dtype)

arrtype = arrtype.astype(np.string_)

print(arrtype)


