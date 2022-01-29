import random

def jogar():

    print("********************************")
    print("Bem vindo ao Jogo de Advinhacao!")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000
    print("Qual nivel de dificuldade?")
    print("(1) FACIL (2) MEDIO (3) DIFICIL")
    print("********************************")
    nivel = int(input("Definir nivel: "))
    print("********************************")

    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre 1 e 100, e tente acertar o Numero Secreto: ")

        print("Voce digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Voce Acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Voce errou!! O seu chute foi MAIOR que o numero secreto!")
                print("********************************")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos.".format(
                        numero_secreto, pontos))
            elif (menor):
                print("Voce errou!! O seu chute foi MENOR que o numero secreto!")
                print("********************************")
                if (rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {} pontos.".format(
                        numero_secreto, pontos))
                    print("********************************")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()