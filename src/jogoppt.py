import random


def jogar():
    regras_jogo()

    while (True):
        print("Escolha entre: \n 1. Pedra \n 2. Papel \n 3.Tesoura")
        print("*************************************")

        escolha = int(input("Sua Escolha: "))

        while (escolha > 3 or escolha < 1):
            escolha = int(input("Entre com um numero valido: "))

        if escolha == 1:
            n_escolha = 'Pedra'
        elif escolha == 2:
            n_escolha = 'Papel'
        elif escolha == 3:
            n_escolha = 'Tesoura'

        print("Sua escolha e: " + n_escolha)
        print("\nTurno do computador... ")

        escolha_bot = random.randint(1, 3)
        while (escolha_bot == escolha):
            escolha_bot = random.randint(1, 3)

        if escolha_bot == 1:
            bot_nome = 'Pedra'
        elif escolha_bot == 2:
            bot_nome = 'Papel'
        elif escolha_bot == 3:
            bot_nome = 'Tesoura'

        print("A escolha do computador e: " + bot_nome)
        print(n_escolha + " Vs " + bot_nome)

        if ((escolha == 1 and escolha_bot == 2) or (escolha == 2 and escolha_bot == 1)):
            print("PAPEL VENCEU!!! >>>", end="")
            resultado = "Papel"
        elif ((escolha == 1 and escolha_bot == 3) or (escolha == 3 and escolha_bot == 1)):
            print("PEDRA VENCEU!! >>>", end="")
            resultado = "Pedra"
        else:
            print("TESOURA VENCEU!!! >>>", end="")
            resultado = "Tesoura"

        if (resultado == n_escolha):
            print("<<<<===JOGADOR VENCEU =D ===>>>>")
        else:
            print("<<<<===COMPUTADOR VENCEU =( ===>>>>")

        print("Gostaria de jogar novamente? (S/N)")
        ans = input()

        if ans == 'n' or ans == 'N':
            break

    print("Obrigado por jogar!! Experimente nossos outros jogos!")


def regras_jogo():
    print("*** Regras do jogo Pedra, Papel e Tesoura *** \n"
          + "- Pedra GANHA de Tesoura\n"
          + "- Tesoura GANHA de Papel \n"
          + "- Papel GANHA de Pedra \n")
    print("*************************************")


if (__name__ == "__main__"):
    jogar()
