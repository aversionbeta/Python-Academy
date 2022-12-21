
# imprimir variable

edad = 31
print (f"Mi edad es de {edad} años")

# Conversión de tipo de datos 

x=3.3 
y= 1.1 + 2.2
yfloat=round(y,1)

print (x)
print (y)
print(yfloat)
print(x==y)
print(yfloat==x)

# Validando a través de True or False 

cantidadreq=input("Por favor ingrese la cantidad que necesita:  ")
stock=100
agotado=f"Lo sentimos. Actualmente no contamos con la cantidad que necesitas pero trabajaremos la próxima vez para garantizar la cantidad que necesitas. Actualmente contamos con {stock} unidades, por favor haga su pedido por una cantidad igual o menor a esta."
confirmado=f"Tu pedido de {cantidadreq} UND va en camino! No dudes en escribirnos para cualquier solicitud adicional."
if int(cantidadreq) > int(stock):
    print(agotado)
else:
    print(confirmado)

#Operadores en cadenas de texto
text="Yo aprendo a programar en Python"
text2="yo aprendo a programar en python"
print('JS' in text)
print('Python' in text)
print('python' in text)

size=len(text)
print(size)

print(text.upper())
print(text.lower())
print(text.count('a'))
print(text.swapcase())
print(text.startswith('Y'))
print(text.endswith('n'))
print(text.replace('Python', 'HTML'))
print(text2.capitalize())
print(text2.title())
print(text[1])
print(text[0])
print(text[size-1])
print(text[-1])
print(text[0:2])
print(text[:2])
print(text[:-1])
print(text[2:])
print(text[0:2:1])
print(text[0:5:3])


#Listas - igual a arrays en JS

number=[1,2,3,4,5,6]
print(number)
print(number[2:4])

number[0]=2
print(number)

#CRUD de listas 
number=[1,2,3,4,5,6]
number[0]=2
print(number)

number.append(7) #Inserta a la lista en la última posición
print(number)
number.insert(0, 'Prueba') #Inserta a la lista en la posición que le indique
print(number)

number2=[10,11,12,13]
totalnumber=number+number2
print(totalnumber)

print(totalnumber.index(11))

index=totalnumber.index(11) #Cálcula el índice del valor 11
totalnumber[index]=12 #Reemplaza un valor en el índice que le indique
print(totalnumber)

totalnumber.pop()
print(totalnumber)

totalnumber.pop(0)
print(totalnumber)

totalnumber.reverse()
print(totalnumber)

totalnumber.sort() #Ordena de mayor a menor
print(totalnumber)

totalnumber[0]=1
print(totalnumber)

#Tuplas 

numbers=(1,2,3,4,5,5)
print(type(numbers))
print(numbers.index(3))
print(numbers.count(5))

newlist=list(numbers)
newlist.append(6)
print(type(newlist))
print(newlist)

#diccionarios - igual a objetos en JS

my_dict={}
print(type(my_dict))

my_dict={
    'name': ['David'],
    'lastname': ['Betancur', 'Gaviria'],
    'age':32
}

print(my_dict['age'])
print(my_dict['lastname'])
print(my_dict.get('noexiste'))

my_dict['name']= ['Juan']
my_dict['age']+= 1
my_dict['lastname'].append('Uribe')
my_dict['name'].append('David')
my_dict['hobbies']='Jugar'
print(my_dict)

print('items',my_dict.items())
print('keys',my_dict.keys())
print('values',my_dict.values())

del my_dict['age']

print(my_dict)

my_dict.pop('lastname')

print(my_dict)

#while 

counter=0

while counter<10:
    counter+=1
    if counter == 7:
        break
    print(counter)

counter=0

while counter<10:
    counter+=1
    if counter < 7:
        continue
    print(counter)

    counter=0

while counter<10:
    counter+=1
    if counter > 7:
        continue
    print(counter)

#Loops 

for element in range (50):
    print(element)

for element in range (2,50):
    print(element+1)

#Loops con listas y Tuplas

list=[23,45,67,89,90]
for element in list:
    print(element)

tuple=('Juan', 'David', 'Betancur')
for element in tuple:
    print(element)

product={
    'name': 'jean',
    'price': 100,
    'stock': 400
}

for key in product: 
    print(key,'=>',product[key])

for key, value in product.items(): #Lo mismo que la pasada, sólo se define value = product[key]
    print(key,'=>',value)

people=[
    {
        'name': 'David',
        'age': 32
    },
    {
        'name': 'Carlos',
        'age': 70
    },
    {
        'name': 'Luz',
        'age': 65
    }
]

for person in people:
    print('name=>',person['name'])

matriz=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# print(matriz[0])
# print(matriz[0][1])

for row in matriz:
    print(row)
    for item in row:
        print(item)

import this

#set_conjuntos

numbers=[1,2,3,4,5,6,1,2,3,4,5]
set_numbers = set(numbers)
print(set_numbers)
print(type(set_numbers))
list_numbers=list(set_numbers)
set_numbers = set(numbers)
print(list_numbers)
print(type(list_numbers))
size=len(set_numbers)
print(size)
print(7 in set_numbers)
set_numbers.add(7) #agregar elementos al conjunto
print(set_numbers)
set_numbers.update({8,9,10}) #actualizar elementos en el conjunto
print(set_numbers)
set_numbers.remove(10) #remover elementos en el conjunto
print(set_numbers)
set_numbers.clear()
print(set_numbers) #limpiar todo el conjunto


#operaciones entre conjuntos 

set_num1={1,2,3,4,5,6,10}
set_num2={6,7,8,9,10}
set_num3={10,11,12,13}
set_num4=set_num1.union(set_num2)
print(set_num4)
set_num5=(set_num1|set_num2|set_num3) #unión de conjuntos
print(set_num5)
set_num6=set_num1.intersection(set_num2) #intersección de conjuntos
set_num9=(set_num1&set_num2&set_num3)
print(set_num6)
print(set_num9)
set_num7=set_num1.difference(set_num2) #diferencia
set_num10=(set_num1-set_num2-set_num3)
print(set_num7)
print(set_num10)
set_num8=set_num1.symmetric_difference(set_num2) #diferencia simétrica (unicón sin los elementos que tienen en común)
set_num11=(set_num1^set_num2^set_num3)
print(set_num8)
print(set_num11)

#List Comprehensions

numbers_v1=[]
for element in range(1,11):
    numbers_v1.append(element)
print(numbers_v1)

numbers_v2 = [element for element in range (1,11)]
print(numbers_v2)

numbers_v2 = [element*2 for element in range (1,11)]
print(numbers_v2)

numbers_v3=[]
for i in range(1,11):
    if i % 2 == 0:
        numbers_v3.append(i*2)

print(numbers_v3)

numbers_v4=[i*2 for i in range(1,11) if i%2 ==0]
print(numbers_v4)

#dictionary comprenhensions

dict = {}
for i in range (1,5):
    dict[i] = i*2
print(dict)

################

dict_v2 = {i: i*2 for i in range (1,5)}
print(dict_v2)

################

import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries: 
    population[country] = random.randint(1,1000)
print(population)

####################

import random
countries = ['col', 'mex', 'bol', 'pe']
population={country:random.randint(1,1000) for country in countries }
print(population)

###################
names=['juan', 'david', 'andrés']
ages= [12,15,18]

print(list(zip(names,ages)))

####################

names=['juan', 'david', 'andrés']
ages= [12,15,18]

dict={names:ages for (names,ages) in zip(names,ages)}
print(dict)

####################

import random
countries = ['col', 'mex', 'bol', 'pe']

population_v2={country: random.randint(1,100) for country in countries }
print(population_v2)

result={country: population for (country,population) in population_v2.items() if population>50}
print(result)

##################

text = 'Hola mi nombre es Juan David'

vowel = {c:c.upper() for c in text if c in 'aeiou'}
print(vowel)

# Funciones 

def suma(a,b):
    print(a+b)

suma(2,10)
suma(2,8)

################

def sum_with_for(a,b):
    sum=0
    for x in range (a,b):
        sum += x
    print(sum)

sum_with_for(1,2)
sum_with_for(1,20)

#Funciones con valores por defecto 

def volume(height=1,width=1,depth=1):
    return height*width*depth

result = volume()  
print(result)  

#########

def volume(height=1,width=1,depth=1):
    return height*width*depth, width, 'Resultado'

result, widht, text = volume(width=10)

print(result)
print(widht)  
print(text)

#lambda

full_name = lambda name, last_name : f'El nombre completo es {name.title()} {last_name.title()}'
text= full_name('juan', 'david')
print (text)

#HOF

def increment(x):
    return x + 1

def hof(x,func):
    return x + func(x)

result = hof(2,increment)

print(result)

###########

increment = lambda x: x+1

hof = lambda x, func: x+func(x)

result = hof(2,increment)
print(result)