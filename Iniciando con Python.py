
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


