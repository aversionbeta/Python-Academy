# Piedra papel o tijeras 

import random 

options= ('Piedra', 'Papel', 'Tijera')

pcscore=0
userscore=0
rounds=1

while True: 
    print('*'* 10)
    print('ROUND', round)
    print('*'* 10)

    print('PC Score:', pcscore)
    print('User Score', userscore)

    username= input("Introduzca su nombre: ")
    userselec=input("Introduzca la palabra: Piedra, Papel o Tijera para jugar => ")
    pcselec=random.choice(options)
    pcwins=print(f"Usted ha escogido {userselec} y la máquina ha escogido {pcselec}. La Máquina gana")
    userwins=print(f"Usted ha escogido {userselec} y la máquina ha escogido {pcselec}. {username} gana")
    tie=print(f"La selección de la máquina ha sido {pcselec} y la suya {userselec}. Hay un Empate")

    if not userselec in options:
        print('Esta opción no es válida, por favor elija una opción correcta')
        continue

    print('User option =>', userselec)
    print('Computer´s option', pcselec)

    if userselec==pcselec:
        tie
    elif userselec=="Piedra": 
        if pcselec=="Tijera":
            userwins
            userscore+1
    elif userselec=="Piedra": 
        if pcselec=="Papel":
            pcwins
            pcscore+1
    elif userselec=="Papel": 
        if pcselec=="Piedra":
            userwins
            userscore+1
    elif userselec=="Piedra": 
        if pcselec=="Tijera":
            userwins
            userscore+1
    elif userselec=="Tijera": 
        if pcselec=="Piedra":
            pcwins
            pcscore+1
    elif userselec=="Papel": 
        if pcselec=="Tijera":
            pcwins
            pcscore+1
    elif userselec=="Tijera": 
        if pcselec=="Papel":
            userwins
            userscore+1
    else: 
        print("Error al introducit el valor. Asegurese que no hay espacios")
    if pcscore==2:
        print('El ganador es el PC')
        break 

    if userscore==2:
        print('El ganador es el usuario')
        break 
    round+=1


