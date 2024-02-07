def main(): #A função existe para ser repetida.
    
    super_poderes = ['Invisibilidade', 'Manipulação de Eletricidade', 'Controle do Tempo']

    print("Seja bem-vindo(a) ao código de você cria o seu poder e coloca em uma lista!! Aqui estão os poderes disponíveis:\n\n", super_poderes)
    escolha = input("\nVocê quer criar um poder novo? Sim ou Não?\n>")

    #Essa função é a repetição, pois ela chama a função main() causando um looping.

    def rep():
        novamente = input("\nVocê deseja criar outro poder? Sim ou Não?\n>")

        if novamente == "Sim" or "sim" or "s":
            main()
            super_poderes.append()

        elif novamente == "Não" or "não" or "nao" or "n":
            print("Ok")

    #Esse if é o que ativa a repetição.

    if escolha == "Sim" or "sim" or "s":

        nome_poder = input("\nDigite o nome do seu poder:\n>")
        super_poderes.append(nome_poder)

        print(super_poderes)
        rep()

    elif escolha == "Não" or "não" or "nao" or "n":
        print("Ok, volte sempre.")

    return
main()
