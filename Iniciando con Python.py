
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


#Listas 

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


