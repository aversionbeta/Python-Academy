import random

def selec_option():
    option=('PIEDRA', 'PAPEL', 'TIJERA')
    selec_user=input('Piedra, Papel o Tijera? => ')
    selec_user=selec_user.upper()

    if not selec_user in option:
        print('Por favor seleccione una opción válida o verifique la escritura de la opción')
        return None, None
        
    selec_pc=random.choice(option)

    print('Usuario juega con => ', selec_user)
    print('Usuario juega con => ', selec_pc)
    return selec_user,selec_pc

def game_rules(selec_user,selec_pc, pc_score, user_score):
    if selec_user==selec_pc:
        print('Empate!')
    elif selec_user=='PIEDRA':
        if selec_pc=="PAPEL":
            print('Papel gana a Piedra')
            print('Gana PC')
            pc_score +=1 
        if selec_pc == 'TIJERA':
            print('Piedra gana a Tijera')
            print('Gana Usuario')
            user_score +=1
    elif selec_user=='PAPEL':
        if selec_pc=='PIEDRA':
            print('Papel gana a Piedra')
            print('Gana Usuario')
            user_score +=1
        elif selec_pc=='TIJERA':
            print('Tijera gana a Papel')
            print('Gana PC')
            pc_score +=1 
    elif selec_user=='TIJERA':
        if selec_pc=='PIEDRA':
            print('Piedra gana a Tijera')
            print('Gana PC')
            pc_score +=1 
        if selec_pc=='PAPEL':
            print('Tijera gana a Papel')
            print('Gana Usuario')
            user_score +=1
    return pc_score, user_score

def run_game():
    pc_score=0
    user_score=0
    rounds=1
    while True:
        print('*'*10)
        print('ROUND',rounds)
        print('*'*10)

        print('Puntos Usuario', user_score)
        print('Puntos PC', pc_score)
        rounds+=1

        selec_user,selec_pc = selec_option()
        pc_score, user_score=game_rules(selec_user,selec_pc, pc_score, user_score)

        if pc_score==2:
            print('El ganador es el PC')
            break
        
        if user_score==2:
            print('El ganador es el usuario')
            break

run_game()