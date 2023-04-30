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

#Creando arrays 

arr_c=list(range(0,10,2))
print (arr_c)

import numpy as np
np.arange(0,10,2)
np.zeros(5)
np.zeros((10,5))
np.ones((10,5))
np.linspace(0,10,10)
np.linspace(0,10,100)
np.eye(4)
np.random.rand(4)
np.random.rand(4,4)
np.random.randint(4,100,(10,10))

#Shape and Reshape

import numpy as np

arr_shape=np.random.randint(1,10,(3,2))
arr_shape.shape
arr_shape.reshape(1,6)
np.reshape(arr_shape,(2,3),'C')
np.reshape(arr_shape,(2,3),'F')
np.reshape(arr_shape,(2,3),'A')

#Principal Functions

import numpy as np

arr_pf=np.random.randint(1,9,10)
matriz_pf=arr_pf.reshape(2,5)
arr_pf.max()
arr_pf.max(0)
print(matriz_pf)
matriz_pf.max(0)
matriz_pf.max(1)
arr_pf.min()
arr_pf.min(0)
print(matriz_pf)
matriz_pf.min(0)
matriz_pf.min(1)
matriz_pf.argmin()
matriz_pf.ptp()
print(arr_pf)
np.percentile(arr_pf,50)
np.percentile(arr_pf,25)
np.median(arr_pf)
np.std(arr_pf)
np.var(arr_pf)
np.mean(arr_pf)
a=np.array([[1,2],[3,4]])
b=np.array([6,7])
a.ndim
b.ndim
b=np.expand_dims(b,axis=0)
np.concatenate((a,b),axis=0)
np.concatenate((a,b.T),axis=1)
b
b.T

#Copy
import numpy as np
copy = np.arange(0,11)
slicing_arr = copy.copy[0:6]
slicing_arr
slicing_arr[:]=0
slicing_arr
copy

#Conditions

import numpy as np
con=np.linspace(1,10,10, dtype='int8')
index_conditions=con>5
con[index_conditions]
con[(con>5)&(con<9)]

#Operations

import numpy as np
lista=[1,2]
lista
lista *2
arr=np.arange(0,10)
arr2=arr.copy()
arr
arr*2
arr+2
arr**2
arr+arr2
matriz = arr.reshape(2,5)
matriz2=matriz.copy()
matriz
matriz+matriz
np.matmul(matriz,matriz2.T)
matriz@matriz2.T





