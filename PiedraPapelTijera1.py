# Piedra papel o tijeras 

username= input("Introduzca su nombre: ")
userselec=input("Introduzca la palabra: Piedra, Papel o Tijera para jugar => ")
pcselec="Piedra"
pcwins=print(f"Usted ha escogido {userselec} y la máquina ha escogido {pcselec}. La Máquina gana")
userwins=print(f"Usted ha escogido {userselec} y la máquina ha escogido {pcselec}. {username} gana")
tie=print(f"La selección de la máquina ha sido {pcselec} y la suya {userselec}. Hay un Empate")

if userselec==pcselec:
    tie
elif userselec=="Piedra": 
    if pcselec=="Tijera":
        userwins
elif userselec=="Piedra": 
    if pcselec=="Papel":
        pcwins
elif userselec=="Papel": 
    if pcselec=="Piedra":
        userwins
elif userselec=="Piedra": 
    if pcselec=="Tijera":
        userwins
elif userselec=="Tijera": 
    if pcselec=="Piedra":
        pcwins
elif userselec=="Papel": 
    if pcselec=="Tijera":
        pcwins
elif userselec=="Tijera": 
    if pcselec=="Papel":
        userwins
else: 
    print("Error al introducit el valor. Asegurese que no hay espacios")


