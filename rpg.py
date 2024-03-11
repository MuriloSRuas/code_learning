#Variáveis e Import

from random import randint

round = 1

player_forca = 5
player_vida = 20
player_escudo = 5

player = [player_vida , player_forca , player_escudo]

dragon_forca = 7
dragon_vida = 30

dragon = [dragon_vida , dragon_forca]


#Jogo

print("\tVocê está em uma missão mortal de matar um dragão que destroiu a cidade, o rei Rodolfo o enviou sem esperança alguma de vitória, pois quem realmente acreditaria que um homem pudesse vencer um dragão? Ainda mais que todos os \"guerreiros mais fortes\" do reino não aceitaram a missão, porque julgavam ser impossível de conseguir completar tal missão ridícula. Eles falaram isso porque estavam com medo. Mas você é diferente, você aceitou a missão mortal sem pensar duas vezes, agora não tem mais volta. Quando você saiu da vila com o seu cavalo e suas armas, o pessoal da vila o chamaram de \"louco\".")
print("\tNo caminho, você escuta um rugido de longe e uma fumaça subindo das árvores. Você vai lá e não encontra nada, além de umas árvores e o chão queimados. Você ia sair de lá, mas, do nada você sente uma pressão absurda vindo de trás de você, era o dragão que parecia ter uns 5 metros de altura nas 4 patas; e com um comprimento de aproximadamente de 8 metros, ele te encarava nos olhos pronto para te matar. Você paralisa e entra em um dilema, Fugir ou Lutar.")
print("\nEscolha: Fugir(1) ou Lutar(2).")

dilema = input(">")

def dado(): #Dado d10
    dado = randint(1,10)
    return dado

def ataque(character):  #Beyond 
    if character == player:
        dice_bonus = dado()
        golpe = player[1] + dice_bonus
        print(f"Dado: {dice_bonus}. Você lançou um golpe no dragão e causou {golpe} de dano.")
        return golpe

    elif character == dragon:
        golpe = dragon[1] + dado()
        return golpe

def esquiva(dragon_attack):

    esquiva = dado()
    print(esquiva)

    if esquiva >= dragon_attack:
        return print(f"Dado {esquiva}, você esquivou.")
    
    elif esquiva < dragon_attack:
        vida = (player[0] + player[2] + esquiva) - dragon_attack

        if dragon_attack >= 5:
            player[0] = vida
            player[2] = 0
            vida = (player[0] + esquiva) - dragon_attack 
        
        else:
            print("Erro.")

        return print(f"Dado: {esquiva}, você não conseguiu desviar totalmente e recebeu um dano de {dragon_attack}. Com isso, vocẽ ficou com {vida} pontos de vida.")
    
    elif esquiva == 1:
        return print(f"Dado: {esquiva}, você quase morreu por pouco, levou {dragon_attack} de dano. Com isso você ficou com {vida} pontos de vida.")
    
    else:
        return print("Vou entender isso como desistencia.")


if "1" in dilema:
    
    print("Você tenta fugir, mas o seu cavalo não é rápido o suficiente, porque o dragão voa. Ele cospe fogo na sua direção, você aceita a morte ou tenta defender?")
    print("\nEscolha: Aceitar(1) ou Defender(2).")

    escolha = input("\n>")

    if "1" in escolha:
        print("Você aceitou a morte, e morreu...")

    elif "2" in escolha:
        roll = dado()
        
        if roll < 5:
            print("Você lutou bravamente contra o medo, mas o seu corpo não acompanhou.")
            
        elif roll > 5:
            print("Você sente uma sensação estranha dentro de você, mas você por algum motivo se sente mais forte, então você tenta cortar o fogo, e ele se dissipa. O dragão olha para vocẽ e sente uma pressão poderosa e recua um pouco.")
            print("O resto dessa batalha vai ser história, infelizmente não posso passar daqui, o jogo ia ficar muito longo kkkkkkkkkk.")

elif "2" in dilema:
    
    while round:
        print("\nRound ", round)
        print(f"Dragão LV ??: \n\tVida: {dragon[0]} \nVocê: \n\tVida: {player[0]} \n\t Escudo: {player[2]}")
        dragon_attack = ataque(dragon)
        print("O dragão te ataca, com o poder de: ", dragon_attack)

        choice = input("Você esquiva? Se sim, digite 1.\n>")

        if choice == "1":
            esquiva(dragon_attack)
            
            choice = input("Você ataca? Se sim, digite 1.\n>")

            if choice == "1":
                attack = ataque(player)
                dragon[0] = dragon[0] - attack

            else:
                print("Bobeou perdeu.")
                break
        
        else:
            print("Ok, você morre então.")
            break

        if player[0] <= 0:
            player[0] = 0
            print(f"\nResultado de batalha:\n\tDragão LV ??: \n\tVida: {dragon[0]} \nVocê: \n\tVida: {player[0]} \n\t Escudo: {player[2]}")
            print("\nVocê lutou bravamente e morreu.")
            break
        
        elif dragon[0] <= 0:
            dragon[0] = 0
            print(f"\nResultado de batalha:\nDragão LV ??: \n\tVida: {dragon[0]} \nVocê: \n\tVida: {player[0]} \n\t Escudo: {player[2]}")
            print("\nParabéns guerreiro, você venceu o dragão!!")
            break

        else:
            round += 1

else:
    print("Erro, não entendi o que você quis dizer com isso.")